from langchain.prompts import PromptTemplate

def load_prompt(prompt_template: str, input_variables: list) -> PromptTemplate:
    """This function returns a PromptTemplate object"""
    return PromptTemplate(
            input_variables=input_variables,
            template=prompt_template
    )