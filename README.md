# Manning Project: Adding Knowledge to a Chatbot with RAG

## Overview

This project implements a Retrieval-Augmented Generation (RAG) Chemistry Assistant using Qdrant, Nomic Embeddings, Llama 3.1, WasmEdge, and LlamaEdge.

The system converts chemistry textbook content into vector embeddings, stores them in a Qdrant vector database, retrieves relevant knowledge through semantic search, and injects the retrieved context into prompts before generating responses.

The project follows the Manning liveProject workflow for building a domain-specific chatbot with external knowledge.

---

## Project Objective

The objective of this project is to build a chemistry-focused AI assistant that:

* Uses external chemistry knowledge
* Stores vector embeddings in Qdrant
* Retrieves relevant knowledge using semantic similarity search
* Enhances LLM responses using retrieved context
* Provides grounded and domain-specific answers

---

## Technology Stack

* Llama 3.1 8B Instruct (GGUF)
* Nomic Embed Text v1.5
* Qdrant Vector Database
* WasmEdge Runtime
* LlamaEdge RAG API Server
* CSV-based QA Knowledge Indexing

---

## System Architecture

```text
Chemistry Textbook
        ↓
QA Generation
        ↓
chemistry-by-chapter.csv
        ↓
Nomic Embeddings
        ↓
Qdrant Vector Database
        ↓
RAG API Server
        ↓
Llama 3.1
        ↓
OpenAI-Compatible API
        ↓
Chemistry Assistant
```

---

## Project Workflow

### Milestone 1 – Create Vector Database

* Installed and started Qdrant using Docker
* Created the chemistry collection
* Configured cosine similarity search
* Verified collection status

### Milestone 2 – Generate QA Dataset

* Downloaded chemistry textbook chapters
* Generated question-answer indexed content
* Created chemistry-by-chapter.csv

### Milestone 3 – Generate Embeddings

* Downloaded Nomic embedding model
* Generated 768-dimensional embeddings
* Embedded QA pairs for semantic search

### Milestone 4 – Store Vectors in Qdrant

* Uploaded embeddings into Qdrant
* Stored source chapter text as payload
* Verified collection contents

### Milestone 5 – Start RAG API Server

* Downloaded rag-api-server.wasm
* Connected Llama 3.1 model
* Connected embedding model
* Configured Qdrant retrieval

### Milestone 6 – Test Retrieval-Augmented Responses

* Verified OpenAI-compatible API endpoint
* Queried the system with chemistry questions
* Confirmed retrieval and response generation

---

## Deliverables

* chemistry-by-chapter.csv
* collection_status.txt
* chemistry_snapshot.zip
* rag_response.txt
* vectors_from_paragraph_chemistry.py

---

## Challenges Faced

* Docker daemon startup issues
* Qdrant collection configuration
* Gaia endpoint availability problems
* Local model integration
* Embedding generation performance
* Retrieval quality optimization
* Prompt and context configuration

---

## Learning Outcomes

Through this project, I learned:

* Retrieval-Augmented Generation (RAG)
* Vector embeddings
* Semantic search
* Qdrant vector databases
* Nomic embedding models
* WasmEdge runtime
* LlamaEdge API servers
* Context injection techniques
* OpenAI-compatible API development
* End-to-end RAG system architecture

---

## Result

Successfully built a Retrieval-Augmented Generation (RAG) Chemistry Assistant that uses a vector database for external knowledge retrieval and generates context-aware responses through a Llama 3.1 language model.

