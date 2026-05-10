import requests
import streamlit as st

# Function
def get_open_llm_response(input_text):

    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={
            'input': {
                'topic': input_text
            }
        }
    )

    return response.json()['output']

# Streamlit UI
st.title("Chatbot with LangChain and Ollama")

input_text = st.text_input("Ask a question:")

if input_text:
    st.write(get_open_llm_response(input_text))