from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model="llama3.1"
)

chat_history = []

system_message = SystemMessage(content="You are a helpful AI assisstant")
chat_history.append(system_message)

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))

    result = llm.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("----Message History----")
print(chat_history)
