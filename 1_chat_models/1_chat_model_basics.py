from dotenv import load_dotenv
from langchain_ollama import ChatOllama
import os

load_dotenv()

llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    base_url=os.getenv("OLLAMA_API_BASE")
)

result = llm.invoke("What is 81 divided by 9?")

print("Full result:")
print(result)
print("Content only:")
print(result.content)
