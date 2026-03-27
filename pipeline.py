from src.transcribe import get_content, get_video_id
from src.chunker import chunk_content, prepare_transcript
from src.embedder import create_embeddings
import time
import random

urls = [
    (""
    "", "transcripts/what_is_neural_network.txt"),
    ("https://www.youtube.com/watch?v=wjZofJX0v4M", "transcripts/transformers.txt"),
    ("https://www.youtube.com/watch?v=fHF22Wxuyw4", "transcripts/what_is_deep_learning.txt"),
    ("https://www.youtube.com/watch?v=C6YtPJxNULA", "transcripts/all_about_ml_and_dl.txt")
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