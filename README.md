# Manning LiveProject – Adding Knowledge to a Chatbot with RAG

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline using:

- Qdrant Vector Database
- Nomic Embed Text v1.5
- Llama 3.1 8B
- WasmEdge
- LlamaEdge RAG API Server

The goal is to enhance a chatbot with chemistry knowledge by indexing textbook content into a vector database and retrieving relevant context during question answering.

---

## Architecture

Chemistry Textbook
        │
        ▼
QA Generation Script
(vectors_from_paragraph_chemistry.py)
        │
        ▼
chemistry-by-chapter.csv
        │
        ▼
Nomic Embedding Model
        │
        ▼
Qdrant Vector Database
        │
        ▼
rag-api-server.wasm
        │
        ▼
Llama 3.1
        │
        ▼
Chemistry Answers

---

## Technologies Used

- Qdrant
- Nomic Embed Text v1.5
- Llama 3.1 8B
- WasmEdge
- LlamaEdge
- Python
- Retrieval Augmented Generation (RAG)

---

## Deliverables

### Generated Dataset

- chemistry-by-chapter.csv

### Collection Status

- collection_status.txt

### Snapshot

- chemistry_snapshot.zip

### RAG Response

- rag_response.txt

### Screenshots

Located in the screenshots folder.

---

## Results

Successfully:

- Created a chemistry vector collection
- Generated QA-based retrieval data
- Stored vectors in Qdrant
- Retrieved chapter content from vector search
- Started a RAG-enabled API server
- Queried the knowledge base through the OpenAI-compatible API

---

## Author

Krishna Bharadwaj
