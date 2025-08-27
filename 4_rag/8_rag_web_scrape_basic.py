import os

from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
# WebBaseLoader needs bs4 installed and PyPDFLoader needs pypdf installed
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables from .env file
load_dotenv()

# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "db")
pdf_dir = os.path.join(current_dir, "pdf", "somatosensory.pdf")
persistent_directory = os.path.join(db_dir, "chroma_db_apple")
persistent_pdf_directory = os.path.join(db_dir, "chroma_db_pdf")

urls = ["https://www.apple.com/"]

# Create a loader for the web content
loader = WebBaseLoader(urls)
documents = loader.load()

# Create a loader for the pdf content
pdf_loader = PyPDFLoader(pdf_dir)
pdf_documents = pdf_loader.load()

# Step 2: Split the scraped content into chunks
# CharacterTextSplitter splits the text into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
pdf_docs = text_splitter.split_documents(pdf_documents)

# Display information about the split documents
print("\n--- Document Chunks Information ---")
print(f"Number of document chunks: {len(docs)}")
print(f"Sample chunk:\n{docs[0].page_content}\n")

print("\n--- PDF Document Chunks Information ---")
print(f"Number of document chunks: {len(pdf_docs)}")
print(f"Sample chunk:\n{pdf_docs[0].page_content}\n")

# Step 3: Create embeddings for the document chunks
# Create embeddings using Hugging Face BGE model
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

# Step 4: Create and persist the vector store with the embeddings
# Chroma stores the embeddings for efficient searching
if not os.path.exists(persistent_directory):
    print(f"\n--- Creating vector store in {persistent_directory} ---")
    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=persistent_directory
    )
    print(f"--- Finished creating vector store in {persistent_directory} ---")
else:
    print(f"Vector store {persistent_directory} already exists. No need to initialize.")
    db = Chroma(
        persist_directory=persistent_directory,
        embedding_function=embeddings
    )

if not os.path.exists(persistent_pdf_directory):
    print(f"\n--- Creating vector store in {persistent_pdf_directory} ---")
    db_pdf = Chroma.from_documents(
        pdf_docs,
        embeddings,
        persist_directory=persistent_pdf_directory
    )
    print(f"--- Finished creating vector store in {persistent_pdf_directory} ---")
else:
    print(f"Vector store {persistent_pdf_directory} already exists. No need to initialize.")
    db_pdf = Chroma(
        persist_directory=persistent_pdf_directory,
        embedding_function=embeddings
    )

# Step 5: Query the vector store
# Create a retriever for querying the vector store
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

retriever_pdf = db_pdf.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Define the user's question
query = "What new products are announced on Apple.com?"

# Retrieve relevant documents based on the query
relevant_docs = retriever.invoke(query)

pdf_query = "What is somatosensory?"

relevant_pdf_docs = retriever_pdf.invoke(pdf_query)

# Display the relevant results with metadata
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get("source", "Unknown")}\n")

print("\n--- PDF Relevant Documents ---")
for i, doc in enumerate(relevant_pdf_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get("source", "Unknown")}\n")
