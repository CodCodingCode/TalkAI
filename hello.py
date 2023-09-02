import streamlit as st
from PIL import Image

st.set_page_config(page_title="TalkAI", page_icon=":globe_with_meridians", layout="wide")
st.header('st.button')
with st.container():
     if st.button('+ What is TalkAI?'):
          st.write('TalkAI uses top-of-the-line technology to connect everyone across the world.')
          st.write("Its free translation features language barrier issues much easier to solve")
          st.write("TalkAI was created to tackle to everlasting issues of accessibility in our countries,")
          st.write("though language barriers in different areas.")
     else:
          st.write('Goodbye')


st.subheader("what is this")


st.write("hello 2")
st.write("helloplease")



