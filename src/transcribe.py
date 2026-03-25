from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os
load_dotenv()


def get_video_id(url):
    if "v=" in url:
        video_id = url.split("v=")[-1].split('&')[0] # timestamp case (real url links)
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1] # links shared from whatsapp or telegram
    else:
        raise ValueError(f"Could not extract the video ID from URL:{url}")
    return video_id


def get_content(video_id,fallback_file=None):
    try:
        api = YouTubeTranscriptApi()
        transcripts = api.fetch(video_id,languages=['en','hi'])
        doc = [(line.text,line.duration,line.start) for line in transcripts]
        return doc
    except Exception as e:
        print(f"API failed: {e}")
    print("Using fallback_file...")    
    if fallback_file:
        with open(fallback_file,'r') as f:
            lines = f.readlines()

        doc = []
        i = 0
        while i<len(lines):
            line = lines[i].strip()
            if not line:
                i+=1
                continue
            if i+1<len(lines):
                next_line = lines[i+1].strip()
                if ':' in next_line:
                    minutes,seconds = next_line.split(":")
                    start = int(minutes) * 60 + int(seconds)
                    doc.append((line,0,start))
                    i+=2
                    continue
            doc.append((line,0,0))
            i+=1
        return doc
    return ValueError("No content available from API or fallback")