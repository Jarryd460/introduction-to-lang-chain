# Introduction to LangChain

This repository serves as a comprehensive introduction to working with LangChain's chat models, featuring multiple model providers and interaction patterns. It includes practical examples demonstrating various aspects of chat model integration, from basic usage to advanced conversation handling.

The examples support multiple model providers including:
- **Ollama** (local LLMs)
- **Anthropic** (Claude models)
- **Hugging Face** (hosted models)

Each example is designed to be self-contained and demonstrates a specific aspect of working with LangChain's chat model interface.

## 🚀 Features

- Basic implementation of LangChain's chat model interface
- Integration with Ollama's LLaMA models
- Environment variable management with python-dotenv
- Poetry for dependency management
- Multiple example scripts demonstrating different chat model capabilities
- Prompt template examples for structured LLM interactions
- Chain implementations for complex LLM workflows

## 📦 Prerequisites

- Python 3.13+
- [Poetry](https://python-poetry.org/) for dependency management
- [Ollama](https://ollama.com/) installed and running locally (optional, for local embeddings)
- Ollama LLaMA model downloaded (e.g., `llama3.1`) (optional)
- For Hugging Face embeddings:
  - Install `sentence-transformers`: `poetry add sentence-transformers`
  - Recommended model: `BAAI/bge-small-en` (automatically downloaded on first use)

## 🛠️ Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/introduction-to-lang-chain.git
   cd introduction-to-lang-chain
   ```

2. Activate the environment and install dependencies:
   ```bash
   poetry env activate
   ```
   Run the output of the above command to activate the environment. 

   Example output (default location of virtual environment): C:\Users\JarrydDeane\AppData\Local\pypoetry\Cache\virtualenvs\introduction-to-lang-chain-PrWevuoM-py3.13

   It is possible to also have the environment live in the root directory of this project by adding the following to the poetry.toml file (create it if it doesn't exist):

   ```toml
   [virtualenvs]
   in-project = true
   ```

   ```bash
   poetry install
   ```

3. Create a `.env` file in the root directory and add your environment variables:
   ```env
   # Example .env file
   OLLAMA_API_BASE=http://localhost:11434
   ```

4. Ensure you have the required Ollama model downloaded:
   ```bash
   ollama pull llama3.1
   ```

## 🚀 Usage

### Available Chat Model Examples

1. **Basic Chat Model** (`1_chat_model_basics.py`)
   - Initialize and use a chat model with Ollama
   - Basic message passing and response handling
   - Example: Simple math problem solving

2. **Basic Conversation** (`2_chat_model_basic_conversation.py`)
   - Maintain conversation history with multiple turns
   - Structure messages with system and human roles
   - Build context-aware conversations
   - Example: Multi-turn math problem solving

3. **Model Alternatives** (`3_chat_model_alternatives.py`)
   - Compare different LLM providers:
     - Ollama (local models)
     - Anthropic (Claude models)
     - Hugging Face (hosted models)
   - Configure different model parameters
   - Handle different response formats

4. **Interactive Conversation** (`4_chat_model_conversation_with_user.py`)
   - Implement an interactive chat interface
   - Manage conversation state and history
   - Handle user input and model responses
   - Example: Interactive AI assistant with memory

## 🎯 Prompt Templates

### 1. Basic Prompt Templates (`2_prompt_templates/1_prompt_template_basic.py`)
- Create and use simple prompt templates with placeholders
- Work with multiple placeholders in a single template
- Build structured prompts with system and human messages
- Example: Generating jokes with dynamic topics and counts
- Example: Creating multi-part prompts with different message types

### 2. Chat Model Integration (`2_prompt_templates/2_prompt_template_with_chat_model.py`)
- Integrate prompt templates with LangChain's chat models
- Create dynamic, parameterized prompts for chat interactions
- Build complex conversation flows with structured messages
- Example: Story generation with customizable parameters
- Example: Interactive Q&A with system context

## ⛓️ Chains

### 1. Basic Chains (`3_chains/1_chains_basics.py`)
- Create sequential chains using the pipe operator (`|`)
- Combine prompt templates with LLMs and output parsers
- Build reusable processing pipelines
- Example: Joke generation with dynamic topics and counts
- Demonstrates LangChain Expression Language (LCEL) fundamentals

### 2. Understanding Chains (`3_chains/2_chains_under_the_hood.py`)
- Explore the underlying mechanics of chains
- Implement custom Runnable components
- Manually create and connect chain steps
- Understand how LCEL simplifies chain creation

### 3. Extended Chains (`3_chains/3_chains_extended.py`)
- Add custom processing steps to chains
- Chain multiple transformations together
- Implement type-safe operations with RunnableLambda
- Example: Text processing with uppercase conversion and word count
- Shows how to extend chains with custom logic

### 4. Parallel Processing (`3_chains/4_chains_parallel.py`)
- Execute multiple chains in parallel
- Combine and process results from parallel executions
- Implement branching with RunnableParallel
- Example: Product review analysis with simultaneous pros/cons evaluation
- Demonstrates efficient parallel processing patterns

### 5. Branching Logic (`3_chains/5_chains_branching.py`)
- Implement conditional routing in chains
- Create dynamic execution paths with RunnableBranch
- Handle different input types with appropriate processing
- Example: Customer feedback classification and routing system
- Shows how to build complex decision trees in LangChain

## 🔍 RAG (Retrieval-Augmented Generation)

### 1. Basic RAG Implementation (`4_rag/1a_rag_basics.py` and `4_rag/1b_rag_basics.py`)
- **Document Processing**
  - Loading and preprocessing text documents
  - Chunking strategies for optimal retrieval
  - Document metadata management
- **Vector Store**
  - Setting up ChromaDB for document storage
  - Configuring persistent storage
  - Managing document embeddings
- **Embedding Models**
  - Default: `BAAI/bge-small-en`
  - Configurable device (CPU/GPU)
  - Normalization options
  - Batch processing support
- **Query Pipeline**
  - Similarity search implementation
  - Result filtering and ranking
  - Response generation

### 2. RAG with Metadata (`4_rag/2a_rag_basics_metadata.py` and `4_rag/2b_rag_basics_metadata.py`)
- **Metadata Integration**
  - Document source tracking
  - Custom metadata fields
  - Metadata-based filtering
- **Advanced Retrieval**
  - Filtering by document properties
  - Source attribution
  - Result scoring with metadata
- **Performance**
  - Efficient metadata storage
  - Optimized retrieval with filters
  - Batch processing support

### 3. Text Splitting Deep Dive (`4_rag/3_rag_text_splitting_deep_dive.py`)
- **Splitting Strategies**
  - Character-based (fixed size chunks)
  - Sentence-aware splitting
  - Token-based splitting
  - Recursive character splitting
  - Custom splitter implementation
- **Analysis**
  - Chunk size impact
  - Overlap configuration
  - Performance comparison
  - Quality metrics

### 4. Embedding Deep Dive (`4_rag/4_rag_embedding_deep_dive.py`)
- **Model Configuration**
  - Hugging Face model selection
  - Device optimization (CPU/GPU)
  - Normalization techniques
  - Batch processing options
- **Performance**
  - Embedding generation
  - Storage optimization
  - Query performance
  - Memory management

### 5. Retriever Deep Dive (`4_rag/5_rag_retriever_deep_dive.py`)
- **Search Strategies**
  - Similarity search (top-k)
  - Max Marginal Relevance (MMR)
  - Score threshold filtering
- **Parameters**
  - Result count (k)
  - MMR fetch size
  - Diversity adjustment (lambda)
  - Minimum score thresholds
- **Use Cases**
  - When to use each strategy
  - Performance implications
  - Quality vs diversity tradeoffs

### 6. One-off Question Answering (`4_rag/6_rag_one_off_question.py`)
- **Pipeline**
  - Query processing
  - Context retrieval
  - Response generation
- **Model**
  - DeepSeek model integration
  - Generation parameters
  - Response formatting
- **Features**
  - Fallback handling
  - Source attribution
  - Confidence scoring

### 7. Conversational RAG (`4_rag/7_rag_conversational.py`)
- **Conversation Management**
  - Multi-turn context handling
  - Chat history persistence
  - Context window management
- **Advanced Retrieval**
  - History-aware queries
  - Contextual reformulation
  - Dynamic retrieval adjustment
- **Response Generation**
  - Conversational flow
  - Context integration
  - Natural follow-up handling
- Configuring conversation chains with LangChain's building blocks:
  - History-aware retriever
  - Document processing chain
  - Chat prompt templates
- Managing conversation state and message history
- Customizing system prompts for better conversation flow

### Running Examples

You can run any of the examples using either method:

**With activated environment:**
```bash
python 1_chat_models/1_chat_model_basics.py
```

**Using Poetry:**
```bash
poetry run python 1_chat_models/1_chat_model_basics.py
```

For the interactive conversation example, use:
```bash
python 1_chat_models/4_chat_model_conversation_with_user.py
```

## 🔧 Useful Commands

### Environment Management

- Activate the virtual environment:
  ```bash
  poetry env activate
  # Then run the command shown in the output to activate the environment
  ```

- Get the path to the virtual environment:
  ```bash
  poetry env info --path
  ```

- Configure the virtual environment to be in the root directory of the project (Creates a poetry.toml file if it doesn't exist):
  ```bash
  poetry config virtualenvs.in-project true --local
  ```

  or

- Configures it globally (Applies to all projects). Creates config.toml file in %APPDATA%\pypoetry
  ```bash
  poetry config virtualenvs.in-project true
  ```

- Install dependencies:
  ```bash
  poetry install
  ```

- Add a new dependency:
  ```bash
  poetry add package-name
  ```

- Update all dependencies:
  ```bash
  poetry update
  ```

### Ollama Commands

- List available models:
  ```bash
  ollama list
  ```

- Pull a specific model:
  ```bash
  ollama pull model-name
  ```

- Run a model directly:
  ```bash
  ollama run model-name
  ```

## 📚 Additional Resources

- [LangChain Crash Course](https://github.com/bhancockio/langchain-crash-course/tree/main/4_rag) - A comprehensive crash course on LangChain's RAG (Retrieval-Augmented Generation) implementation, including practical examples and best practices.

## 📁 Project Structure

```
introduction-to-lang-chain/
├── 1_chat_models/               # Directory containing chat model examples
│   ├── 1_chat_model_basics.py            # Basic chat model initialization and usage
│   ├── 2_chat_model_basic_conversation.py # Demonstrates conversation history
│   ├── 3_chat_model_alternatives.py       # Shows different model configurations
│   └── 4_chat_model_conversation_with_user.py  # Interactive chat interface
├── 2_prompt_templates/          # Directory containing prompt template examples
│   ├── 1_prompt_template_basic.py         # Basic prompt template usage
│   └── 2_prompt_template_with_chat_model.py # Templates with chat model integration
├── 3_chains/                    # Directory containing chain examples
│   ├── 1_chains_basics.py                # Basic chain implementation with pipe operator
│   ├── 2_chains_under_the_hood.py         # Detailed chain implementation showing internals
│   ├── 3_chains_extended.py              # Advanced chain operations with type hints
│   ├── 4_chains_parallel.py              # Running multiple chains in parallel
│   └── 5_chains_branching.py             # Conditional logic with branching chains
├── 4_rag/                        # Directory containing RAG examples
│   ├── 1a_rag_basics.py                  # Basic RAG implementation setup
│   ├── 1b_rag_basics.py                  # Querying the basic RAG system
│   ├── 2a_rag_basics_metadata.py         # RAG with metadata support
│   ├── 2b_rag_basics_metadata.py         # Querying RAG with metadata filters
│   ├── 3_rag_text_splitting_deep_dive.py # Comparing text splitting strategies
│   ├── 4_rag_embedding_deep_dive.py      # Exploring embedding models and configs
│   ├── 5_rag_retriever_deep_dive.py     # Comparing retrieval strategies
│   ├── 6_rag_one_off_question.py        # Complete Q&A pipeline example
│   ├── 7_rag_conversational.py          # Multi-turn conversational RAG system
│   ├── books/                            # Sample text documents for RAG
│   └── db/                               # Vector store database directory
├── .env                        # Environment variables (create this file)
├── .env.example                # Example environment variables template
├── poetry.lock                 # Poetry lock file (auto-generated)
├── poetry.toml                 # Poetry configuration
├── pyproject.toml              # Project metadata and dependencies
└── README.md                   # This documentation file
```

Each Python file in the `1_chat_models/` directory demonstrates a different aspect of working with LangChain's chat models, progressing from basic to more advanced usage patterns.

## 📚 Dependencies

### Core Dependencies
- `langchain` (>=0.3.27,<0.4.0) - Core framework for building LLM applications
- `langchain-ollama` (>=0.3.6,<0.4.0) - Ollama integration for LangChain
- `python-dotenv` (>=1.1.1,<2.0.0) - Loads environment variables from .env files

### Version Management
- `poetry` - Dependency management and packaging

### Environment Variables
The following environment variables are used in the examples:
- `OLLAMA_API_BASE`: Base URL for the Ollama API (default: http://localhost:11434)
- `ANTHROPIC_API_KEY`: Api key needed for accessing Claude models
- `HUGGINGFACEHUB_API_TOKEN`: Token for accessing models on hugging face
