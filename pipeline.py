from src.transcribe import get_content, get_video_id
from src.chunker import chunk_content, prepare_transcript
from src.embedder import create_embeddings
import time
import random

urls = [
    ("https://www.youtube.com/watch?v=aircAruvnKk", "transcripts/what_is_neural_network.txt"),
    ("https://www.youtube.com/watch?v=wjZofJX0v4M", "transcripts/transformers.txt"),
    ("https://www.youtube.com/watch?v=fHF22Wxuyw4", "transcripts/what_is_deep_learning.txt"),
    ("https://www.youtube.com/watch?v=C6YtPJxNULA", "transcripts/all_about_ml_and_dl.txt")
]

def main():
    all_chunks = []

    for url, fallback_file in urls:
        try:
            video_id = get_video_id(url)

            # Use fallback file if API fails
            content = get_content(video_id, fallback_file)

            transcript, metadata = prepare_transcript(content)
            chunks = chunk_content(transcript, metadata)

            all_chunks.extend(chunks)
            print(f"Done: {url}")

            time.sleep(random.randint(2, 5))

        except Exception as e:
            print(f"Skipped: {url} | Error: {e}")
            continue

    create_embeddings(all_chunks)
    print("✅ Done FAISS index save!!")


if __name__ == "__main__":
    main()