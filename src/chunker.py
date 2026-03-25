from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken


def prepare_transcript(doc):
    segments = []
    metadata = []
    buffer = []

    for text,_,start in doc:
        segments.append(text)
        metadata.append({'start':start})

    return segments,metadata

def chunk_content(segments,metadata):

    encoder = tiktoken.get_encoding('cl100k_base')

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=60,
        length_function=lambda text: len(encoder.encode(text)) # measuring tool used to decide when to stop if size > chunk_size then cut
        )
    
    chunks = splitter.create_documents(segments,metadatas=metadata)
    return chunks