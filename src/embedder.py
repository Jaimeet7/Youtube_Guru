from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

embedding_model = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

def create_embeddings(chunks):
    db = FAISS.from_documents(chunks,embedding_model)
    db.save_local("faiss_index")
    return db
def load_db():
    db = FAISS.load_local("faiss_index",embedding_model ,allow_dangerous_deserialization=True)
    return db