# YouTube Guru — RAG QA Bot

## Project Overview
A RAG-based QA bot built on transcripts from 4 YouTube videos on neural networks and deep learning. Uses FAISS for vector storage, HuggingFace embeddings, and Gemini 2.0 Flash for generation.

## Tech Stack
- **Scraping** — youtube-transcript-api
- **Chunking** — LangChain RecursiveCharacterTextSplitter
- **Embeddings** — HuggingFace all-MiniLM-L6-v2
- **Vector Store** — FAISS
- **Generation** — Gemini 2.0 Flash
- **UI** — Streamlit

## Project Structure
```
project/
├── src/
│   ├── transcribe.py
│   ├── chunker.py
│   ├── embedder.py
│   └── generator.py
├── pipeline.py
├── app.py
└── transcripts/
```

## Golden Dataset — 5 QA Pairs

### Q1: 
**"What is a neural network and how is it inspired by the human brain?"**
**Answer:**  
**Source & Timestamp:**  

### Q2:
**Question:**  
**Answer:**  
**Source & Timestamp:**  

### Q3:
**Question:**  
**Answer:**  
**Source & Timestamp:**  

### Q4:
**Question:**  
**Answer:**  
**Source & Timestamp:**  

### Q5:
**Question:**  
**Answer:**  
**Source & Timestamp:**  

## Methodology
- **How questions were selected:**
- **How they were pulled from material:**
- **What they are testing:**
- **What a wrong retrieval would look like:**

## How to Run
```bash
pip install -r requirements.txt
python pipeline.py  # build FAISS index
streamlit run app.py  # launch UI
```