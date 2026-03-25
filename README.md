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
**Question:"What is a neural network and how is it inspired by the human brain?"**
**Answer:What is a neural network? The context states, "But what I want to do here is show you what a neural network actually is," but it does not go on to explain what a neural network actually is. Therefore, I don't have enough information to answer this part of the question.

How is it inspired by the human brain? The context explicitly states that "neural networks are inspired by the brain." It further clarifies that this inspiration means they are "loosely analogous to how in biological networks of neurons." This means that the way neural networks are designed and function is meant to be similar, in a general sense, to how the networks of neurons (brain cells) in living organisms work.**

**Source & Timestamp:📍 Sources:

⏱️ 02:48| what_is_neural_network — As the name suggests neural networks are inspired by the brain, but let's break that down....

⏱️ 13:40| what_is_neural_network — This is how you'd see it if you choose to read up more about neural networks....

⏱️ 04:53| what_is_neural_network — It's meant to be loosely analogous to how in biological networks of neurons,...

⏱️ 01:18| what_is_neural_network — But what I want to do here is show you what a neural network actually is,...**  
**  

### Q2:
**Question:"What is the attention mechanism in transformers?"**  
**Answer:The attention mechanism in transformers is responsible for figuring out which parts of the input are most relevant. It's a key component of the transformer architecture, allowing the model to focus on specific aspects of the data. The attention block is where this process takes place, enabling the model to weigh the importance of different inputs. This mechanism helps the transformer to efficiently process and understand complex data.**  
**Source & Timestamp:📍 Sources:

⏱️ 13:12| all_about_ml_and_dl — what is transformer, what is attention...

⏱️ 26:27| transformers — full of tunable parameters, then understanding the attention mechanism,...

⏱️ 00:39| transformers — visually-driven explanation for what actually happens inside a transformer....

⏱️ 04:15| transformers — The attention block is what's responsible for figuring out which...**
**  

### Q3:
**Question:"What is backpropagation and how does it work?"**  
**Answer:Backpropagation is a method used to train neural networks, specifically referring to the backward propagation of errors. It's a key component in training feed forward neural networks, allowing them to learn from their mistakes. Unfortunately, the details of how it works are not provided in this context, as it was discussed in previous chapters. We would need to refer to those previous chapters for a more detailed explanation of the backpropagation process.**

 
**Source & Timestamp:📍 Sources:

⏱️ 09:22| transformers — it's called backpropagation, we talked about it in previous chapters,...

⏱️ 12:08| all_about_ml_and_dl — we have feed forward neural networks...

⏱️ 13:43| all_about_ml_and_dl — how your neural network is trained...

⏱️ 12:10| all_about_ml_and_dl — we have backward propagation methods...**

### Q4:
**Question:"What is deep learning and how is it different from machine learning?"**  
**Answer:Deep learning is a class of models that is a subset of machine learning. It is mentioned alongside AI, indicating a relationship between the three concepts. Unfortunately, the provided context does not explicitly explain how deep learning differs from machine learning, only that deep learning is a specific type of model. I don't have enough information to fully elaborate on the differences.**

**Source & Timestamp:📍 Sources:

⏱️ 11:12| all_about_ml_and_dl — Now you will say that you have told basic machine learning, but what is AI, what is deep learning, w...

⏱️ 09:13| transformers — Deep learning describes a class of models that in the...

⏱️ 01:09| all_about_ml_and_dl — you want to save your career. What is machine learning?...

⏱️ 14:13| all_about_ml_and_dl — so this was some basics of machine learning, AI and deep learning...**  

### Q5:
**Question:"What are the layers in a neural network and what do they do?"**  
**Answer:A neural network consists of multiple layers, but the context doesn't specify the exact functions of each layer. However, it does mention connections between one layer and a particular neuron in the next layer, implying that layers are connected in a sequential manner. The context also hints that the speaker is about to explain what a neural network is, but doesn't provide a clear explanation of the layers. I don't have enough information to provide a detailed explanation of the layers and their functions.**

**Source & Timestamp:📍 Sources:

⏱️ 13:43| all_about_ml_and_dl — how your neural network is trained...

⏱️ 13:58| what_is_neural_network — to the connections between one layer and a particular neuron in the next layer....

⏱️ 12:54| all_about_ml_and_dl — a kind of neural network...

⏱️ 01:18| what_is_neural_network — But what I want to do here is show you what a neural network actually is,... **  

## Methodology
- **How questions were selected:**
** Questions were designed to simulate a real user interaction, which focused on conceptual understanding. This ensured the coverage of a wide range of domains. **
- **How they were pulled from material:**
** Questions were answered using a retrieval-based approach. Relevant transcript chunks were extracted using semantic similarity search over vector embeddings generated from the video transcripts.**
- **What they are testing:**
** 	•	The effectiveness of semantic retrieval
	•	The model’s ability to generate context aware responses
    •	The system’s handling of varied query types (generic, specific, and reference-based)
	•	The accuracy of source attribution (timestamps and transcript alignment)**
- **What a wrong retrieval would look like:**
** 	•	Irrelevant transcript chunks being selected 
	•	Missing context required to answer the question
    •	Redundant or repetitive chunks 
    •	Incorrect or misleading timestamps **

## How to Run
```bash
pip install -r requirements.txt
python pipeline.py  # build FAISS index
streamlit run app.py  # launch UI
```