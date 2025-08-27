from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

# Create a prompt template
template = "Tell me a joke about {topic}"
# Create a chat prompt template from the template
prompt_template = ChatPromptTemplate.from_template(template)

# Invoke the prompt template with the topic
prompt = prompt_template.invoke({"topic": "dogs"})
print("----Prompt from Template----")
# Print the prompt
print(prompt)

# Create a prompt template with multiple placeholders
template_multiple = """You are a helpful assistant
Human: Tell me a {adjective} story about a {animal}.
Assistant:"""

# Create a chat prompt template from the template
prompt_template_multiple = ChatPromptTemplate.from_template(template_multiple)
# Invoke the prompt template with the topic
prompt = prompt_template_multiple.invoke({"adjective": "scary", "animal": "cow"})
print("----Prompt with multiple placeholders----")
# Print the prompt
print(prompt)

# Create a prompt template with system and human messages (Tuple)
messages = [
    ("system", "You are a comedian who tell jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
    # Placeholders {joke_count} are not replaced in prompts when using HumanMessage, SystemMessage or AIMessage.
    # If there is no placeholders in template then you can use HumanMessage, SystemMessage or AIMessage.
    # HumanMessage(content="Tell me {joke_count} jokes.")
]

# Create a chat prompt template from the messages
prompt_template = ChatPromptTemplate.from_messages(messages)
# Invoke the prompt template with the topic
prompt = prompt_template.invoke({"topic": "deer", "joke_count": 3})
print("----Prompt with system and human messages (Tuple)----")
# Print the prompt
print(prompt)
