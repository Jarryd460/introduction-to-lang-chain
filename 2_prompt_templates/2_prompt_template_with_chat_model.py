from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# Load environment variables from .env file
load_dotenv()

# Create llm model to be used
llm = ChatOllama(
    model="llama3.1"
)

print("----Prompt from template----")
# Create a prompt template
template = "Tell me a story about {topic}"
# Create a chat prompt template from the template
prompt_template = ChatPromptTemplate.from_template(template)

# Invoke the prompt template with the topic
prompt = prompt_template.invoke({"topic": "cats"})
# Invoke the llm model with the prompt
result = llm.invoke(prompt)
# Print the result
print(result.content)

print("----Prompt with multiple placeholders----")
# Create a prompt template with multiple placeholders
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} short story about a {animal}.
Assistant:"""
# Create a chat prompt template from the template
prompt_template_multiple = ChatPromptTemplate.from_template(template_multiple)
# Invoke the prompt template with the topic
prompt = prompt_template_multiple.invoke({"adjective": "scary", "animal": "cat"})
# Invoke the llm model with the prompt
result = llm.invoke(prompt)
# Print the result
print(result.content)

print("----Prompt with system and human messages (Tuple)----")
# Create a prompt template with system and human messages (Tuple)
messages = [
    ("system", "You are a mad scientist who invents {topic}"),
    ("human", "What is the {adjective} you've invented?")
]
prompt_template = ChatPromptTemplate.from_messages(messages)

# Invoke the prompt template with the topic
prompt = prompt_template.invoke({"topic": "mutated animals", "adjective": "weirdest"})
# Invoke the llm model with the prompt
result = llm.invoke(prompt)
# Print the result
print(result.content)
