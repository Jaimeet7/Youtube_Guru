from src.transcribe import get_content,get_video_id
from src.chunker import chunk_content,prepare_transcript
from src.embedder import load_db,create_embeddings
from src.generator import answer
import time


urls = [
    ("https://www.youtube.com/watch?v=aircAruvnKk",None),
    ("https://www.youtube.com/watch?v=wjZofJX0v4M",None),
    ("https://www.youtube.com/watch?v=fHF22Wxuyw4",None),
    ("https://www.youtube.com/watch?v=C6YtPJxNULA",None)
]

all_chunks = []

for url,fallback_file in urls:
    try:
        video_id = get_video_id(url)
        content = get_content(video_id,fallback_file)
        transcript,metadata = prepare_transcript(content)
        chunks = chunk_content(transcript,metadata)
        all_chunks.extend(chunks)
        print(f"Done:{url}")
        time.sleep(3)
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
        print(f"-{chunk.page_content}...| timestamp:{chunk.metadata}")