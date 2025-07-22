import os
from langchain_openai import ChatOpenAI
import streamlit as st

def load_model():
    """This function loads the LLM used for email processing"""
    return ChatOpenAI(
        api_key = st.secrets["OPENAI_API_KEY"],
        model=st.secrets["LLM"]
    )