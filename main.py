import streamlit as st
from few_shot import Few_Shot_Posts
from post_generator import generate_post


fs = Few_Shot_Posts()
st.title("Linkedin Post Generator")

col1, col2 = st.columns(2)

with col1:
    topic = st.selectbox("Topic", options=fs.get_unique_tags())
with col2:
    length = st.selectbox("Length", options=["Short", "Medium", "Long"])

if st.button("Generate"):
    st.write(f"Generated post for {topic}, {length}")
    post = generate_post(length,topic)
    st.write(post)