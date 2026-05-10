from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from huggingface_hub import HfApi
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


#Prompt template

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user","Question: {question}")
])

##Streamlit framework

st.title("Chatbot with Langchain and Hugging Face")
input_text = st.text_input("Ask a question:")

#llm

llm = HuggingFaceEndpoint(
    repo_id="Llama-3.1-8B-Instruct"
)
outputparser = StrOutputParser()
chain = prompt | llm | outputparser

if input_text:
    st.write(chain.invoke({"question": input_text}))

 