# 🚀 LangChain Vector Database Integration

## Overview

This project is a powerful demonstration of integrating LangChain with PostgreSQL's vector database capabilities, enabling advanced semantic search and contextual AI interactions. 🤖✨

## 🌟 Key Features

- **🔍 Semantic Search**: Perform advanced similarity searches on document embeddings
- **🐘 PostgreSQL Integration**: Seamless vector storage using `pgvector`
- **🐳 Dockerized Environment**: Easy setup and deployment
- **🤖 AI-Powered Retrieval**: Generate contextual responses using OpenAI's language models

## 🏗️ Project Architecture

```
📁 langchain-vector-integration/
│
├── 🐳 Dockerfile              # Container configuration
├── 📝 docker-compose.yml       # Multi-container Docker setup
├── 📋 requirements.txt         # Python dependencies
├── 🐍 main.py                  # Core application logic
├── 🗄️ db_setup.py              # Database initialization script
└── 📖 README.md                # Project documentation
```

## 🛠️ Prerequisites

- 🐳 Docker and Docker Compose
- 🔑 OpenAI API Key
- 💻 Basic understanding of Python and vector databases

## 🚀 Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-vector-integration.git
cd langchain-vector-integration
```

### 2. Configure Environment

Create a `.env` file with your credentials:

```env
DATABASE_URL=postgresql://yourusername:yourpassword@postgres:5432/vectordb
OPENAI_API_KEY=your_openai_api_key
```

### 3. Build and Launch 🚢

```bash
docker-compose up --build
```

## 💡 Usage Examples

### Adding Documents to Vector Database

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import PGVector

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create vector store
vectorstore = PGVector(
    connection_string=DATABASE_URL,
    embedding_function=embeddings,
    collection_name="my_documents"
)

# Add documents
documents = [
    "Machine learning is revolutionizing AI",
    "Vector databases enable semantic search"
]

vectorstore.add_texts(documents)
```

### Performing Semantic Search

```python
# Query similar documents
query = "Tell me about AI technologies"
similar_docs = vectorstore.similarity_search(query, k=2)

for doc in similar_docs:
    print(doc.page_content)
```

## 🔬 Advanced Configurations

### Customizing Vector Dimensions

- Default dimension: 1536 (OpenAI's embedding size)
- Modify in `db_setup.py` for different embedding models

### Extending Metadata

Enhance document tracking by adding custom metadata:

```python
vectorstore.add_texts(
    texts=["Your document text"],
    metadatas=[{
        "source": "research_paper.pdf",
        "author": "Jane Doe",
        "timestamp": "2023-08-15"
    }]
)
```

## 🛡️ Troubleshooting

### Common Issues

- **Connection Problems** 🔌
  - Verify `DATABASE_URL` matches Docker Compose settings
  - Check network configurations

- **pgvector Extension** 🐘
  - Ensure PostgreSQL image supports vector extension
  - Use `ankane/pgvector:latest` recommended image

## 📜 License

MIT License - See `LICENSE` file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### 💌 Disclaimer

This project is a demonstration. Ensure compliance with OpenAI's usage policies and adapt the code for production environments.
