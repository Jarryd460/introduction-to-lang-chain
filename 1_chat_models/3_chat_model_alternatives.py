from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline

# Load environment variables from .env file
load_dotenv()

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
# Create messages to be sent to the llm model
messages = [
    # System message to set the context
    SystemMessage(content="Solve the following math problems"),
    # Human message to ask the question
    HumanMessage(content="What is 81 divided by 9?")
]

# Ollama models: https://docs.ollama.com/models
# Automatically pulls in Api Key from environment variable OLLAMA_API_KEY
llm = ChatOllama(
    model="deepseek-r1",
    temperature=0
    # base_url=os.getenv("OLLAMA_API_BASE") excluding url to show it's not needed always as the default value is http://localhost:11434
)

# Invoke the llm model with the messages
result = llm.invoke(messages)
print(f"Answer from DeepSeek: {result.content}")

# Anthropic models: https://docs.anthropic.com/en/docs/models-overview
# Automatically pulls in Api Key from environment variable ANTHROPIC_API_KEY
llm = ChatAnthropic(
    model="claude-opus-4-1-20250805"
)

# Invoke the llm model with the messages
result = llm.invoke(messages)
print(f"Answer from Anthropic: {result.content}")

# Use endpoint to connect to HuggingFace AI models
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto"
)

# Connect to AI models running locally via HuggingFace Pipeline
# Needs all/some of the following installed (didn't investigate which can be removed): text-generation transformers google-search-results numexpr langchainhub sentencepiece jinja2 bitsandbytes accelerate
# Needs a GPU to run based on error message: RuntimeError: No GPU or XPU found. A GPU or XPU is needed for FP8 quantization.
# llm = HuggingFacePipeline.from_model_id(
#     model_id="deepseek-ai/DeepSeek-R1-0528",
#     task="text-generation",
#     pipeline_kwargs=dict(
#         max_new_tokens=512,
#         do_sample=False,
#         repetition_penalty=1.03,
#     ),
# )

# Create chat model to interface with llm
chat_model = ChatHuggingFace(llm=llm)

# Invoke the chat model with the messages
result = chat_model.invoke(messages)
print(f"Answer from Hugging Face: {result.content}")
