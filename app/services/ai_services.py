import os
import logging
from logging.handlers import RotatingFileHandler

from langchain_core.output_parsers import StrOutputParser

from core import config
from loaders.model_loader import load_model
from loaders.prompt_loader import load_prompt
from loaders.runnable_parallel_loader import load_runnable_parallel

handler = RotatingFileHandler('logs/ai_services_log.txt', maxBytes=1000000, backupCount=3)
logging.basicConfig(handlers=[handler], level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Loading model
logging.debug('Initiate model')
model = load_model()

# Summarize Interaction Service
def summarize_interaction_service(email_thread: str, 
                                  summary_notes: str) -> str | None:
    """This function summarizes an email interaction between 
    client and employee.

    Args:
        - email_thread (str): Conversation between client and 
        employee as an email thread
        - summary_notes (str): Employee notes regarding the 
        summary (e.g. summary length, content).
    Returns:
        - string: Email thread summary.
    """
    try:
        logging.debug('Starting "summarize_interaction_service"')

        # Set prompt
        logging.debug('Creating summary prompt')
        prompt = load_prompt(
            config.summary_prompt, 
            ['email_thread', 'summary_notes']
        )

        # Create summry chain
        logging.debug('Creating summary chain')
        chain = prompt | model | StrOutputParser()

        logging.debug('Invoking summary chain')
        response = chain.invoke({
            'email_thread': email_thread, 
            'summary_notes': summary_notes
        })
        return response
    except Exception as e:
        logging.critical(f'Summarization failed: {str(e)}')
    return None



# Suggest Replies Service
def suggest_replies_service(
    email_thread: str,
    employee_notes: str,
    email_tone: str,
    number_of_replies: int
) -> list[str]:
    """This function generates email thread replies using LLMs.

    Args:
        - email_thread (str): Conversation between a cutomer and 
        an empolyee as an email thread.
        - additional_notes (str): Additional instructions given 
        to the model 
        - number_of_replies (int): The number of replies to be 
        generated. Also represents the number of parallel API 
        calls to the LLM.

    Returns:
        - list: A list of generated replies
    """
    try:
        logging.debug('Starting "suggest_replies_service"')
        
        # Load prompt
        logging.debug('Creating suggest replies prompt')
        prompt = load_prompt(
            prompt_template=config.replies_prompt,
            input_variables=['email_thread', 'employee_notes', 'email_tone']
        )
        # Suggest replies chain
        logging.debug('Creating suggest replies chain')
        suggestion_chain = prompt | model | StrOutputParser()

        # Load runnable parallel
        logging.debug(f'Loading runnable parallel')
        runnable = load_runnable_parallel(
            number_of_replies,
            suggestion_chain
        )

        # Invoke runnable to obtain replies
        logging.debug(f'Invoking runnable parallel')
        response = runnable.invoke({
            'email_thread': email_thread,
            'employee_notes': employee_notes,
            'email_tone': email_tone
        })
        logging.debug(f'Runnable response:\n{response}')
        return response
    except Exception as e:
        logging.critical(f'Reply suggestion failed: {str(e)}')



# Generate Follow-Up Email Service
def generate_follow_up_service(
    email_thread: str,
    employee_notes: str,
    email_tone: str,
) -> str:
    """
    """
    try:
        logging.debug('Starting "generate_follow_up_service"')
        
        # Create prompt
        logging.debug('Creating generate follow-up prompt')
        prompt = load_prompt(
            config.generate_prompt,
            input_variables=['email_thread', 'employee_notes', 'email_tone']
        )

        # Create chain
        logging.debug('Creating generate follow-up chain')
        generation_chain = prompt | model | StrOutputParser()

        # Invoke generation chain
        logging.debug('Invoking generate follow-up chain')
        response = generation_chain.invoke({
            'email_thread': email_thread, 
            'employee_notes': employee_notes, 
            'email_tone': email_tone
        })
        return response
    except Exception as e:
        logging.critical(f"Email generation failed: {str(e)}")



