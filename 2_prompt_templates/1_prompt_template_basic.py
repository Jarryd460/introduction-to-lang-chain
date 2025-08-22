from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

template = "Tell me a joke about {topic}"
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic": "dogs"})
print("----Prompt from Template----")
print(prompt)

template_multiple = """You are a helpful assistant
Human: Tell me a {adjective} story about a {animal}.
Assistant:"""

prompt_template_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_template_multiple.invoke({"adjective": "scary", "animal": "cow"})
print("----Prompt with multiple placeholders----")
print(prompt)

messages = [
    ("system", "You are a comedian who tell jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
    # Placeholders {joke_count} are not replaced in prompts when using HumanMessage, SystemMessage or AIMessage.
    # If there is no placeholders in template then you can use HumanMessage, SystemMessage or AIMessage.
    # HumanMessage(content="Tell me {joke_count} jokes.")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "deer", "joke_count": 3})
print("----Prompt with system and human messages (Tuple)----")
print(prompt)

