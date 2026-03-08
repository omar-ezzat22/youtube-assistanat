import streamlit as st
import langchain_helper as lch

st.title("🎥 YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
       
        youtube_url = st.text_area(
            label="What is the YouTube video URL?",
        )
        
        query = st.text_area(
            label="Ask me about the video?",
            key="query"
        )
        
      
        submit_button = st.form_submit_button(label='Submit')


if submit_button:
    if not youtube_url or not query:
        st.warning("Please enter both the YouTube URL and your question.")
    else:
        with st.spinner("جاري تحليل الفيديو والبحث عن الإجابة..."):
       
            db = lch.create_db_from_youtube_video_url(youtube_url)
           
            response, docs = lch.get_response_from_query(db, query)
            
            
            st.subheader("Answer:")
            
            st.write(response)
