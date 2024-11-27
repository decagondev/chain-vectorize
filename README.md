# 🚀 Chain Vectorize: Advanced LangChain Vector Database Integration

## 📝 Overview

Chain Vectorize is a cutting-edge project demonstrating seamless integration of LangChain with PostgreSQL's vector database capabilities. This solution enables advanced semantic search, contextual AI interactions, and efficient document embedding storage.

## 🌟 Key Features

- 🔍 **Semantic Search**: Perform advanced similarity searches on document embeddings
- 🐘 **PostgreSQL Integration**: Robust vector storage using `pgvector`
- 🐳 **Dockerized Environment**: Simplified setup and deployment
- 🤖 **AI-Powered Retrieval**: Contextual response generation with OpenAI's language models
- 📊 **Flexible Metadata Handling**: Store and query document metadata alongside vectors

## 🏗️ Project Structure

```
📁 chain-vectorize/
│
├── 🐳 Dockerfile              # Container configuration
├── 📝 docker-compose.yml       # Multi-container Docker setup
├── 📋 requirements.txt         # Python dependencies
├── 🐍 main.py                  # Core application logic
├── 🗄️ db_setup.py              # Database initialization script
└── 📖 README.md                # Project documentation
```

## 🛠️ Prerequisites

- 💻 Docker and Docker Compose
- 🐍 Python 3.11+
- 🔑 OpenAI API Key
- 🐙 GitHub Account (for contributing)

## 🚀 Quick Start Guide

### 1. Fork the Repository 🍴

1. Visit the repository: https://github.com/decagondev/chain-vectorize
2. Click the **Fork** button in the top-right corner
3. Choose your personal GitHub account

### 2. Clone Your Forked Repository 📦

```bash
# Replace {your-username} with your GitHub username
git clone https://github.com/{your-username}/chain-vectorize.git
cd chain-vectorize

# Add upstream remote
git remote add upstream https://github.com/decagondev/chain-vectorize.git
```

### 3. Set Up Environment Variables 🔧

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://yourusername:yourpassword@postgres:5432/vectordb
OPENAI_API_KEY=your_openai_api_key
```

### 4. Build and Launch 🚢

```bash
docker-compose up --build
```

## 💡 Usage Examples

### Adding Documents to Vector Database

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import PGVector
import os

# Initialize embeddings
embeddings = OpenAIEmbeddings()

# Create vector store
vectorstore = PGVector(
    connection_string=os.getenv("DATABASE_URL"),
    embedding_function=embeddings,
    collection_name="document_collection"
)

# Add documents with metadata
documents = [
    "Machine learning revolutionizes artificial intelligence",
    "Vector databases enable advanced semantic search"
]

metadatas = [
    {"source": "AI_research.txt", "category": "Technology"},
    {"source": "search_tech.pdf", "category": "Database"}
]

vectorstore.add_texts(
    texts=documents,
    metadatas=metadatas
)
```

### Performing Semantic Search

```python
# Query similar documents
query = "Tell me about AI technologies"
similar_docs = vectorstore.similarity_search(query, k=2)

for doc in similar_docs:
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
```

## 🔬 Advanced Configurations

### Customizing Vector Dimensions

- Default dimension: 1536 (OpenAI's embedding size)
- Modify in `db_setup.py` for different embedding models

### Metadata Filtering

```python
# Filter documents by metadata
filtered_docs = vectorstore.similarity_search(
    query="AI",
    filter={"category": "Technology"}
)
```

## 🤝 Contributing Workflow

### Creating a Pull Request

1. **Create a Feature Branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Make Changes**
- Implement your feature
- Add/update tests
- Ensure code quality

3. **Commit Changes**
```bash
git add .
git commit -m "Describe your changes in detail"
```

4. **Sync with Upstream**
```bash
git fetch upstream
git merge upstream/main
```

5. **Push Your Branch**
```bash
git push origin feature/your-feature-name
```

6. **Open Pull Request**
- Go to your fork on GitHub
- Click "New Pull Request"
- Provide a clear description

## 🛡️ Troubleshooting

### Common Issues

- **Database Connection** 🔌
  - Verify `DATABASE_URL` matches Docker Compose settings
  - Check network configurations

- **pgvector Extension** 🐘
  - Ensure PostgreSQL image supports vector extension
  - Recommended: `ankane/pgvector:latest`

## 🚀 Future Roadmap

- [ ] Multi-model embedding support
- [ ] Advanced filtering capabilities
- [ ] Performance monitoring tools
- [ ] Expanded documentation

## 📜 License

MIT License - See `LICENSE` file for details.

## 💌 Disclaimer

This project is a demonstration. Ensure compliance with OpenAI's usage policies and adapt for production environments.

## 🌐 Connect

- **Project Link**: [GitHub Repository](https://github.com/decagondev/chain-vectorize)
- **Issues**: [Project Issues](https://github.com/decagondev/chain-vectorize/issues)

---

**Happy Coding!** 👩‍💻👨‍💻
