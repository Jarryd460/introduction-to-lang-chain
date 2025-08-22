from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model="llama3.1"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tell jokes about {topic}.",),
        ("human", "Tell me {joke_count} jokes.",)
    ]
)

format_prompt = RunnableLambda(lambda x: prompt_template.invoke(x))
invoke_model = RunnableLambda(lambda x: llm.invoke(x))
parse_output = RunnableLambda(lambda x: x.content)

chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

result = chain.invoke({"topic": "lawyers", "joke_count": 3})
print(result)
