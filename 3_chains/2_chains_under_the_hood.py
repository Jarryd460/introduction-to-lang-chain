from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
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
        ("system", "You are a comedian who tell jokes about {topic}.",),
        ("human", "Tell me {joke_count} jokes.",)
    ]
)

# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.invoke(x))
invoke_model = RunnableLambda(lambda x: llm.invoke(x))
parse_output = RunnableLambda(lambda x: x.content)

# Create the RunnableSequence (equivalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Invoke the chain with the topic and joke_count
result = chain.invoke({"topic": "lawyers", "joke_count": 3})

# Print the result
print(result)
