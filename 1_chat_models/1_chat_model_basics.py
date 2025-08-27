from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import os

# Load environment variables from .env file
load_dotenv()

# Create llm model to be used
llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    base_url=os.getenv("OLLAMA_API_BASE")
)

# Invoke the llm model with a question
result = llm.invoke("What is 81 divided by 9?")

# Print the full result and the content of the result
print("Full result:")
print(result)
print("Content only:")
print(result.content)
