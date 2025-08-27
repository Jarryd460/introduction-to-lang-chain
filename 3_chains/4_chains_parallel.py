from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableLambda
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
        SystemMessage(content="You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}.")
    ]
)

# Define the pros analysis step
def analyze_pros(features: str):
    pros_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You are an expert product reviewer"),
            ("human", "Given these features: {features}, list the pros of these features.")
        ]
    )

    return pros_template.format_prompt(features=features)

# Define the cons analysis step
def analyze_cons(features: str):
    cons_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You are an expert product reviewer."),
            ("human", "Given these features: {features}, list the cons of these features.")
        ]
    )
    
    return cons_template.format_prompt(features=features)

# Combine the pros and cons into a final review
def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\nCons:\n{cons}"

# Create the chains for the pros and cons analysis
pros_branch_chain: RunnableLambda[str, str] = RunnableLambda(lambda x: analyze_pros(x)) | llm | StrOutputParser()
cons_branch_chain: RunnableLambda[str, str]= RunnableLambda(lambda x: analyze_cons(x)) | llm | StrOutputParser()

# Create the combined chain using LangChain Expression Language (LCEL)
# Create the chain for the main review
chain = (prompt_template 
        | llm
        | StrOutputParser()
        | RunnableParallel(steps__={"pros": pros_branch_chain, "cons": cons_branch_chain})
        | RunnableLambda(lambda x: combine_pros_cons(x["pros"], x["cons"]))
        # Instead of setting steps directly, you can pass in your own dictionary of key/value pairs which get changed to Runnables internally
        # This is because of **kwargs which accepts dictionary. A Union is also used internal which allows different types to be passed in  
        # | RunnableParallel(branches={"pros": pros_branch_chain, "cons": cons_branch_chain})
        # | RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))
)

# Invoke the chain with the product name
# Response takes a long time
result = chain.invoke({"product_name": "MacBook Pro"})

# Print the result
print(result)
