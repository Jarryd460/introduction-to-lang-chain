from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema import SystemMessage
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableLambda
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(
    model="llama3.1"
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}.")
    ]
)

def analyze_pros(features: str):
    pros_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You are an expert product reviewer"),
            ("human", "Given these features: {features}, list the pros of these features.")
        ]
    )

    return pros_template.format_prompt(features=features)


def analyze_cons(features: str):
    cons_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="You are an expert product reviewer."),
            ("human", "Given these features: {features}, list the cons of these features.")
        ]
    )
    
    return cons_template.format_prompt(features=features)

def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\nCons:\n{cons}"

pros_branch_chain: RunnableLambda[str, str] = RunnableLambda(lambda x: analyze_pros(x)) | llm | StrOutputParser()
cons_branch_chain: RunnableLambda[str, str]= RunnableLambda(lambda x: analyze_cons(x)) | llm | StrOutputParser()

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

# Response takes a long time
result = chain.invoke({"product_name": "MacBook Pro"})
print(result)