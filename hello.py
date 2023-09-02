import streamlit as st
from PIL import Image

st.sidebar.radio('Choose:',[1,2]

st.set_page_config(page_title="TalkAI", page_icon=":globe_with_meridians", layout="wide")
st.header('st.button')
with st.container():
     left, mid, right = st.columns([1, 1, 1])
     with left:
          if st.button('+ What is TalkAI?'):
               st.write('TalkAI uses top-of-the-line technology to connect everyone across the world.')
               st.write("Its free translation features make problems like language barriers much easier to solve.")
               st.write("TalkAI was created to tackle to everlasting issues of accessibility in our countries,")
               st.write("though language barriers in different areas.")
     with mid:
          if st.button("+ Is TalkAI free?"):
               st.write("Yes")
     with right:
          if st.button("+ Does TalkAI use Streamlit?"):
               st.write("yes!")
          



st.subheader("what is this")


st.write("hello 2")
st.write("helloplease")



