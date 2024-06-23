import os
import uvicorn
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_community.llms import Ollama


from dotenv import load_dotenv
load_dotenv()
os.environ['LANGCHAIN_TRACING_V2'] = "True"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

app = FastAPI(
    title = "Langchain-Server",
    version = "1.0.0",
    description = "A simple Langchain Server"
)

add_routes(
    app,
    Ollama(),
    path = "/ollama",
    )

model = Ollama(model = 'mistral')
llm = Ollama(model = 'gemma')

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

add_routes(app,
    prompt1 | model,
    path = '/essay'
)

add_routes(app,
           prompt2 | llm,
           path = '/poem')


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)