import streamlit as st
from PIL import Image

st.title("hello")

img1 = Image.open("/Users/owner/Downloads/Images/Image1.jpeg")

st.subheader("what is this")


st.write("hello 2")
st.write("helloplease")
st.image(img1)



