from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

from dotenv import load_dotenv
load_dotenv()

import os
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "True"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

#Setting up streamlit webpage
import streamlit as st
st.title('LANGCHAIN DEMO WITH OPENAI API')
input_text = st.text_input("Search the topic u want")

#OLLama LLM
llm = Ollama(model='gemma')
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))