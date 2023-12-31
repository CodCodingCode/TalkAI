import streamlit as st
import numpy as np
from PIL import Image
import streamlit as st
import requests


st.set_page_config(page_title="Verticai", page_icon=":globe_with_meridians", layout="wide")
l, r, m = st.columns([1, 1, 1])
with r: 
     st.header('Verticai')

with st.container():
     left, mid, right = st.columns([1, 1, 1])
     with left:
          if st.button('+ What is Verticai?'):
               st.write('Verticai uses top-of-the-line technology to connect everyone across the world.')
               st.write("Its free translation features make problems like language barriers much easier to solve.")
               st.write("Verticai was created to tackle to everlasting issues of accessibility in our countries,")
               st.write("though language barriers in different areas.")
     with mid:
          if st.button("+ Is Verticai free?"):
               st.write("Yes, Verticai is completely free! However, there will be a paid version")
               st.write("to enhance the quality of those who seek better education.")
     with right:
          if st.button("+ Does Verticai use Streamlit?"):
               st.write("Yes! Streamlit's extremely compatible website capabilities")
               st.write("help out with the web creation at Verticai!")


st.header("People from everywhere aroun the world don't have access to solid education")


with st.chat_message("user"):
    st.write("Verticai's Education AI")


# Display a chat input widget.
st.chat_input("Input your textbook url")
