from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import Runnable, RunnableLambda
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model="llama3.1"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes.")
    ]
)

# added Runnable[str, str] so that x can be type safe
uppercase_output: Runnable[str, str] = RunnableLambda(lambda x: x.upper())

# Can also use RunnableLambda to set the type of the input (x) and output (return type of function)
word_count: RunnableLambda[str, str] = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

chain = prompt_template | llm | StrOutputParser() | uppercase_output | word_count

result = chain.invoke({"topic": "lawyers", "joke_count": 3})

print(result)
