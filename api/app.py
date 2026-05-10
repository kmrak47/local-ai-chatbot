from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import uvicorn

# Load environment variables
load_dotenv()

# FastAPI app
app = FastAPI(
    title="LangChain Server",
    description="API for chatbot using LangChain and Ollama",
    version="1.0.0"
)

# LLM
llm = Ollama(model="llama2")

# Basic route
add_routes(
    app,
    llm,
    path="/llama2"
)

# Prompt template
prompt1 = ChatPromptTemplate.from_template(
    "Write an essay about {topic} in 100 words."
)

# Chain route
add_routes(
    app,
    prompt1 | llm,
    path="/essay"
)

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
