from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
import os

# Load environment variables
load_dotenv()

# Create llm model to be used
llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    base_url=os.getenv("OLLAMA_API_BASE")
)

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
# Create messages to be sent to the llm model
messages = [
    # System message to set the context
    SystemMessage(content="Solve the following math problems"),
    # Human message to ask the question
    HumanMessage(content="What is 81 divided by 9?")
]

# Invoke the llm model with the messages
result = llm.invoke(messages)
print(f"Answer from AI: {result.content}")

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
# Create messages to be sent to the llm model
messages = [
    # System message to set the context
    SystemMessage(content="Solve the following math problems"),
    # Human message to ask the question
    HumanMessage(content="What is 81 divided by 9?"),
    # AI message to answer the question - this should be added from result.content but it's been added manually for now
    AIMessage(content="81 divided by 9 is 9"),
    # Human message to ask another question
    HumanMessage(content="What is 10 times 5?")
]

# Invoke the llm model with the messages
result = llm.invoke(messages)
print(f"Answer from AI: {result.content}")
