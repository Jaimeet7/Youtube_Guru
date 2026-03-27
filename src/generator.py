from langchain_groq import ChatGroq
from src.embedder import load_db
from dotenv import load_dotenv
from itertools import cycle
import os
load_dotenv()

api_keys = [
    os.getenv('GROQ_API_KEY_1'),
    os.getenv('GROQ_API_KEY_2'),
    os.getenv('GROQ_API_KEY_3'),
    os.getenv('GROQ_API_KEY_4')
    ]

key_cycle = cycle(api_keys)


def answer(query):
    db = load_db()
    chunks = db.similarity_search(query,top_k=6)

    context = "\n\n".join(chunk.page_content[:300] for chunk in chunks)

    prompt = f"""
    Answer the question based on the context below

    You are a helpful teacher explaining concepts from video transcripts about neural networks and deep learning.
    Give a clear and concise explanation in 3-4 sentences. Use the context below as your source.
    If the answer is not in the context, say "I don't have enough information. 

    Context: {context}

    Question: {query}

    Answer:
    """
    for _ in range(len(api_keys)):
        try:
            llm = ChatGroq(
                model="llama-3.3-70b-versatile",
                groq_api_key=next(key_cycle)
            )
            response = llm.invoke(prompt)
            return response.content,chunks
        except Exception as e:
            if "rate limit" in str(e).lower():
                continue
            else:
                raise e
    raise Exception("all API keys exhausted")