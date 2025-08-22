from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model="llama3.1"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tell jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes.")
    ]
)

chains = prompt_template | llm | StrOutputParser()

result = chains.invoke({"topic": "lawyers", "joke_count": 3})

print(result)