# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI
# from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq
from src.embedder import load_db
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('GROQ_API_KEY')

# llm = ChatGoogleGenerativeAI(
#     model='gemini-1.5-flash',
#     google_api_key=api_key,
#     temperature=0
#     )
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=api_key
)

# llm = ChatOpenAI(model="gpt-4o-mini",api_key=api_key)

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
    response = llm.invoke(prompt)
    return response.content,chunks