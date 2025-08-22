from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model="llama3.1"
)

print("----Prompt from template----")
template = "Tell me a story about {topic}"
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic": "cats"})
result = llm.invoke(prompt)
print(result.content)

print("----Prompt with multiple placeholders----")
template_multiple = """You are a helpful assistant.
Human: Tell me a {adjective} short story about a {animal}.
Assistant:"""
prompt_template_multiple = ChatPromptTemplate.from_template(template_multiple)

prompt = prompt_template_multiple.invoke({"adjective": "scary", "animal": "cat"})
result = llm.invoke(prompt)
print(result.content)

print("----Prompt with system and human messages (Tuple)----")
messages = [
    ("system", "You are a mad scientist who invents {topic}"),
    ("human", "What is the {adjective} you've invented?")
]
prompt_template = ChatPromptTemplate.from_messages(messages)

prompt = prompt_template.invoke({"topic": "mutated animals", "adjective": "weirdest"})
result = llm.invoke(prompt)
print(result.content)
