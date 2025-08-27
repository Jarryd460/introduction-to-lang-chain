from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama import ChatOllama

# Load environment variables from .env file
load_dotenv()

# Create llm model to be used
llm = ChatOllama(
    model="llama3.1"
)

# Create a prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tell jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes.")
    ]
)

# Create the combined chain using LangChain Expression Language (LCEL)
# using pipping automatically calls invoke on the prompt_template, llm and StrOutputParser when the chain is invoked 
chains = prompt_template | llm | StrOutputParser()

# Invoke the chain with the topic and joke_count
result = chains.invoke({"topic": "lawyers", "joke_count": 3})

# Print the result
print(result)