from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_ollama import ChatOllama

# Load environment variables from .env file
load_dotenv()

# Create llm model to be used
llm = ChatOllama(
    model="llama3.1"
)

# Create chat history to be used
chat_history = []

# Create system message to create context
system_message = SystemMessage(content="You are a helpful AI assisstant")
chat_history.append(system_message)

while True:
    # Get user input
    query = input("You: ")

    # Exit if user types exit
    if query.lower() == "exit":
        break

    # Add user input to chat history
    chat_history.append(HumanMessage(content=query))

    # Invoke the llm model with the chat history
    result = llm.invoke(chat_history)

    # Get the response from the llm model
    response = result.content

    # Add the response to the chat history
    chat_history.append(AIMessage(content=response))

    # Print the response
    print(f"AI: {response}")

print("----Message History----")

# Print the chat history
print(chat_history)
