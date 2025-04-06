# Langchain Document Loaders

A comprehensive toolkit for loading and processing various document types using LangChain's document loaders.

## Overview

This repository demonstrates how to use LangChain's document loaders to extract text from different file formats for use in NLP, LLM applications, and AI workflows.

## Installation

```bash
# Clone the repository
git clone https://github.com/Sunilsangfroid/Langchain_document_loaders.git
cd Langchain_document_loaders

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Document Loaders

### PDF Loader

Extract text from PDF documents.

```python
from langchain_community.document_loaders import PyPDFLoader

# Load a PDF
loader = PyPDFLoader("path/to/document.pdf")
docs = loader.load()

# Access content and metadata
print(docs[0].page_content)  # Content of first page
print(docs[0].metadata)      # Metadata of first page
```

### CSV Loader

Process tabular data from CSV files.

```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("path/to/data.csv")
docs = loader.load()
```

### Text Loader

Handle simple text files.

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("path/to/file.txt")
docs = loader.load()
```

### Web Loader

Extract content from websites.

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
docs = loader.load()
```

### Directory Loader

Process multiple files in a directory.

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("./data/", glob="**/*.pdf")
docs = loader.load()
```

## Use Cases

- **Document QA**: Create question-answering systems over document collections
- **Summarization**: Generate summaries of lengthy documents
- **Information Extraction**: Extract structured data from unstructured text
- **Knowledge Base Creation**: Build searchable knowledge bases from document repositories

## Advanced Usage

Each loader can be customized with specific parameters:

```python
# Example: UnstructuredPDFLoader with custom settings
from langchain_community.document_loaders import UnstructuredPDFLoader

loader = UnstructuredPDFLoader(
    "path/to/document.pdf",
    mode="elements",
    strategy="fast"
)
docs = loader.load()
```

## Troubleshooting

Common issues and solutions:

- **Missing dependencies**: Install specific format dependencies (e.g., `pip install "unstructured[pdf]"`)
- **Encoding errors**: Specify encoding with `TextLoader("file.txt", encoding="utf-8")`
- **Memory issues**: Process large documents in chunks using `load_and_split()`

## Environment Setup

To use various LLM providers with your document loaders, create a `.env` file in the root directory and add your API keys:

```bash
# Create .env file
touch .env  # On Windows: type nul > .env
```

Add your API keys to the `.env` file:

```
# OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# Google Gemini
GOOGLE_API_KEY=your_gemini_api_key_here

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Hugging Face
HUGGINGFACE_API_KEY=your_huggingface_api_key_here

# Other configurations
MODEL_NAME=gpt-4-turbo
TEMPERATURE=0.7
```

Load environment variables in your Python code:

```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access keys
openai_api_key = os.getenv("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")
```

Make sure to install python-dotenv:

```bash
pip install python-dotenv
```

Remember to add `.env` to your `.gitignore` file to avoid exposing sensitive keys.

## License

MIT License
