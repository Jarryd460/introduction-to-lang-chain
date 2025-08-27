import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "odyssey.txt")
db_dir = os.path.join(current_dir, "db")

# Ensure the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(
        f"The file {file_path} does not exist. Please check the path."
    )

# Read the text content from the file
loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

# Split the documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Display information about the split documents
print("\n--- Document Chunks Information ---")
print(f"Number of document chunks: {len(docs)}")
print(f"Sample chunk:\n{docs[0].page_content}\n")

# Function to create and persist vector store
def create_vector_store(docs, embeddings, store_name):
    persistent_directory = os.path.join(db_dir, store_name)

    if not os.path.exists(persistent_directory):
        print(f"\n--- Creating vector store {store_name} ---")

        Chroma.from_documents(
            docs,
            embeddings,
            persist_directory=persistent_directory
        )
    else:
        print(f"Vector store {store_name} already exists. No need to initialize.")

# I've only created the Hugging Face embedding demonstration.
# Other embeddings can also be created and demonstrated but I've intentionally left them out as I only have access to free versions from Hugging Face.
# Llama embeddings are extremely slow because it runs on my local machine using Ollama.
print(f"\n--- Using Hugging Face Transformers ---")
huggingface_embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)
create_vector_store(docs, huggingface_embeddings, "chroma_db_huggingface")

print("Embedding demonstrations for Hugging Face completed.")

# Function to query a vector store
def query_vector_store(store_name, query, embedding_function):
    persistent_directory = os.path.join(db_dir, store_name)

    if os.path.exists(persistent_directory):
        print(f"\n--- Querying the Vector Store {store_name} ---")

        db = Chroma(
            persist_directory=persistent_directory,
            embedding_function=embedding_function
        )

        retriever = db.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"k": 3, "score_threshold": 0.1}
        )

        retriever_docs = retriever.invoke(query)

        # Display the relevant results with metadata
        print(f"\n--- Relevant Documents for {store_name} ---")

        for i, doc in enumerate(retriever_docs, 1):
            print(f"Document {i}:\n{doc.page_content}\n")

            if doc.metadata:
                print(f"Source: {doc.metadata.get("source", "Unknown")}\n")
    else:
        print(f"Vector store {store_name} does not exists.")

# Define the user's question
query = "Who is Odysseus' wife?"

# Query each vector store
query_vector_store("chroma_db_huggingface", query, huggingface_embeddings)

print("Query demonstrations completed.")