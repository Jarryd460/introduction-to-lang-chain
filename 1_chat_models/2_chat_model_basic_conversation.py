from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
import os

load_dotenv()

llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    base_url=os.getenv("OLLAMA_API_BASE")
)

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?")
]

result = llm.invoke(messages)
print(f"Answer from AI: {result.content}")

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9"),
    HumanMessage(content="What is 10 times 5?")
]

result = llm.invoke(messages)
print(f"Answer from AI: {result.content}")
