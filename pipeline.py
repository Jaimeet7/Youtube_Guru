from src.transcribe import get_content,get_video_id
from src.chunker import chunk_content,prepare_transcript
from src.embedder import load_db,create_embeddings
from src.generator import answer
import time
import random


urls = [
    ("https://www.youtube.com/watch?v=aircAruvnKk","/Users/jaimeet/Documents/LivoAI project/transcripts/what_is_neural_network.txt"),
    ("https://www.youtube.com/watch?v=wjZofJX0v4M","/Users/jaimeet/Documents/LivoAI project/transcripts/transformers.txt"),
    ("https://www.youtube.com/watch?v=fHF22Wxuyw4","/Users/jaimeet/Documents/LivoAI project/transcripts/what_is_deep_learning.txt"),
    ("https://www.youtube.com/watch?v=C6YtPJxNULA","/Users/jaimeet/Documents/LivoAI project/transcripts/all_about_ml_and_dl.txt")
]

def format_time(seconds):
    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"

all_chunks = []

for url,fallback_file in urls:
    try:
        video_id = get_video_id(url)
        content = get_content(video_id,fallback_file)
        transcript,metadata = prepare_transcript(content)
        chunks = chunk_content(transcript,metadata)
        all_chunks.extend(chunks)
        print(f"Done:{url}")
        time.sleep(random.randint(5,10))
    except Exception as e:
        print(f"Skipped:{url}:{e}")
        continue
db = create_embeddings(all_chunks) 
print("Done FAISS index save!!")
while True:
    query = input("Enter question: ")
    response,chunks = answer(query)
    print(f"Answer:{response}")
    print("Sources:")
    for chunk in chunks:
        start_time = format_time(chunk.metadata.get('start',0))
        print(f"-{chunk.page_content}...| timestamp:{start_time}")