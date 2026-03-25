import streamlit as st
from src.generator import answer



st.title("Youtube Guru 🧑‍🏫")
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
            response, chunks = answer(query)
            st.markdown(response)
            st.markdown("---")
            st.markdown("**📍 Sources:**")
            for chunk in chunks:
                start = chunk.metadata.get("start", 0)
                mins = int(start // 60)
                secs = int(start % 60)
                st.markdown(f"⏱️ `{mins:02d}:{secs:02d}` — {chunk.page_content[:100]}...")

    st.session_state.messages.append({"role": "assistant", "content": response})