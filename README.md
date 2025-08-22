# Introduction to LangChain

This repository serves as an introduction to working with LangChain, specifically focusing on chat models using Ollama's LLaMA models. It includes various examples demonstrating different aspects of chat model interactions.

## 🚀 Features

- Basic implementation of LangChain's chat model interface
- Integration with Ollama's LLaMA models
- Environment variable management with python-dotenv
- Poetry for dependency management
- Multiple example scripts demonstrating different chat model capabilities

## 📦 Prerequisites

- Python 3.13+
- [Poetry](https://python-poetry.org/) for dependency management
- [Ollama](https://ollama.com/) installed and running locally
- Ollama LLaMA model downloaded (e.g., `llama3.1`)

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

### Available Examples

1. **Basic Chat Model** (`1_chat_model_basics.py`)
   - Simple demonstration of initializing and using a chat model
   - Shows basic message passing to the model

2. **Basic Conversation** (`2_chat_model_basic_conversation.py`)
   - Demonstrates maintaining conversation history
   - Shows how to build a back-and-forth conversation

3. **Model Alternatives** (`3_chat_model_alternatives.py`)
   - Demonstrates using different model configurations
   - Shows how to compare outputs from different models

4. **Interactive Conversation** (`4_chat_model_conversation_with_user.py`)
   - Implements an interactive chat interface
   - Shows how to handle user input and model responses

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

## 📁 Project Structure

```
introduction-to-lang-chain/
├── 1_chat_models/               # Directory containing chat model examples
│   ├── 1_chat_model_basics.py            # Basic chat model initialization and usage
│   ├── 2_chat_model_basic_conversation.py # Demonstrates conversation history
│   ├── 3_chat_model_alternatives.py       # Shows different model configurations
│   └── 4_chat_model_conversation_with_user.py  # Interactive chat interface
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
