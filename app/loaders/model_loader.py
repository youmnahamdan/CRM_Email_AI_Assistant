import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def load_model():
    """This function loads the LLM used for email processing"""
    return ChatOpenAI(
        api_key = os.getenv('OPENAI_API_KEY'),
        model=os.getenv('LLM')
    )