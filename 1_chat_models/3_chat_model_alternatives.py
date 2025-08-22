from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFacePipeline

load_dotenv()

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?")
]

llm = ChatOllama(
    model="deepseek-r1",
    temperature=0
    # base_url=os.getenv("OLLAMA_API_BASE") excluding url to show it's not needed always as the default value is http://localhost:11434
)

result = llm.invoke(messages)
print(f"Answer from DeepSeek: {result.content}")

# Anthropic models: https://docs.anthropic.com/en/docs/models-overview
# Automatically pulls in Api Key from environment variable ANTHROPIC_API_KEY
llm = ChatAnthropic(
    model="claude-opus-4-1-20250805"
)

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

chat_model = ChatHuggingFace(llm=llm)
result = chat_model.invoke(messages)
print(f"Answer from Hugging Face: {result.content}")
