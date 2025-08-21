# Introduction to LangChain

This repository serves as an introduction to working with LangChain, specifically focusing on chat models using Ollama's LLaMA models.

## 🚀 Features

- Basic implementation of LangChain's chat model interface
- Integration with Ollama's LLaMA models
- Environment variable management with python-dotenv
- Poetry for dependency management

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

Run the example script:

If you have activated the environment, you can run the script directly:

```bash
python 1_chat_models/1_chat_model_basics.py
```

If you have not activated the environment, you can run the script using poetry:

```bash
poetry run python 1_chat_models/1_chat_model_basics.py
```

This will execute a basic chat completion using the LLaMA model through Ollama.

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
├── 1_chat_models/
│   └── 1_chat_model_basics.py  # Basic chat model implementation
├── .env                        # Environment variables (create this file)
├── poetry.lock                 # Poetry lock file
└── pyproject.toml              # Project dependencies and metadata
```

## 📚 Dependencies

- langchain (>=0.3.27,<0.4.0)
- python-dotenv (>=1.1.1,<2.0.0)
- langchain-ollama (>=0.3.6,<0.4.0)
