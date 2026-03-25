from langchain_google_genai import ChatGoogleGenerativeAI
from src.embedder import load_db
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=api_key,
    temperature=0
    )

def answer(query):
    db = load_db()
    chunks = db.similarity_search(query,top_k=4)

    context = "\n\n".join(chunk.page_content for chunk in chunks)

    prompt = f"""
    Answer the question based on the context below

    Give a thorough, detailed explanation to answer the question. Break it down step by step, use simple language, and make sure the concept is fully understood.
    Use the context below as your source. If the answer is not in the context, say "I don't have enough information to answer this. 
    
    Context: {context}

    Question: {query}

    Answer:
    """
    response = llm.invoke(prompt)
    return response.content,chunks