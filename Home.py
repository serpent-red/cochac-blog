import streamlit as st
import os

st.title("Circle of Care Health Advocacy Blog Page")

post_dir = os.path.listdir("posts")

if len(post_dir) == 0:
  st.write("No posts have been posted yet. Please check back later.")
else:
  for p in post_dir:
    st.write(p)
