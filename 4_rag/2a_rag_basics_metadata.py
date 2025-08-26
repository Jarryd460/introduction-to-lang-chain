import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

current_dir = os.path.dirname(os.path.abspath(__file__))
books_dir = os.path.join(current_dir, "books")
db_dir = os.path.join(current_dir, "db")
persistent_directory = os.path.join(db_dir, "chroma_db_with_metadata")

print(f"Books directory: {books_dir}")
print(f"Persistent directory: {persistent_directory}")

if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    if not os.path.exists(books_dir):
        raise FileNotFoundError(
            f"The directory {books_dir} does not exist. Please check the path."
        )

    book_files = [f for f in os.listdir(books_dir) if f.endswith(".txt")]

    documents = []
    for book_file in book_files:
        file_path = os.path.join(books_dir, book_file)
        loader = TextLoader(file_path, encoding="utf-8")
        book_docs = loader.load()

        for doc in book_docs:
            doc.metadata = {"source": book_file}
            documents.append(doc)

    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0
    )
    docs = text_splitter.split_documents(documents)

    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")

    print("\n--- Creating embeddings ---")
    embeddings = OllamaEmbeddings(
        model ="llama3.1"
    )
    print("\n--- Finished creating embeddings ---")

    print("\n--- Creating and persisting vector store ---")
    # Takes way to long to generate using llama. It ran overnight and was still not complete by the morning
    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=persistent_directory
    )
    print("\n--- Finished creating and persisting vector store ---")
else:
    print("Vector store already exists. No need to initialize.")
