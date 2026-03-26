import streamlit as st
from src.generator import answer

def format_time(seconds):
    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"

st.set_page_config(page_title="YouTube Guru")

st.title("YouTube Guru")
st.markdown("Ask anything about neural networks, transformers, and deep learning!")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response, chunks = answer(query)
                st.markdown(response)
                st.markdown("---")
                st.markdown("### Sources")
                for chunk in chunks:
                    start = chunk.metadata.get("start", 0)
                    source = chunk.metadata.get("source", "unknown")
                    formatted_time = format_time(start)
                    if "v=" in source:
                        video_id = source.split("v=")[-1]
                    else:
                        video_id = source
                    timestamp_url = f"https://www.youtube.com/watch?v={video_id}&t={int(start)}s"
                    st.markdown(
                        f"[{formatted_time}]({timestamp_url}) — {chunk.page_content[:100]}..."
                    )
            except Exception as e:
                st.error("Something went wrong. Please try again.")
                st.exception(e)
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )