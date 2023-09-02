import streamlit as st
import numpy as np
from PIL import Image
import streamlit as st
import requests

st.set_page_config(page_title="Verticai", page_icon=":School", layout="wide")
l, r, m = st.columns([1, 1, 1])
with r: 
     st.markdown("""
     <style>
     .big-font {
         font-size:200px !important;
         text-align: center
     }
     </style>
     """, unsafe_allow_html=True)
     st.markdown('<p class="big-font"> Verticai</p>', unsafe_allow_html=True)
     st.markdown("""
     <style>
     .big-font {
         font-size:50px !important;
         text-align: center
     }
     </style>
     """, unsafe_allow_html=True)
     st.markdown('<p class="big-font"> An AI mentor by your side!</p>', unsafe_allow_html=True)

with st.container():
     left, mid, right = st.columns([1, 1, 1])
     with left:
          if st.button("+ What Is Verticai?"):
               st.write("Verticai uses top-of-the-line technology to help students in need with tutoring and mentorship!")
     with mid:
          if st.button("+ Is Verticai free?"):
               st.write("Yes, Verticai is completely free! However, there will be a paid version to enhance the quality of those who seek better education.")
     with right:
          if st.button("+ Does Verticai use Streamlit?"):
               st.write("Yes! Streamlit's extremely compatible website capabilities help out with the web creation at Verticai!")

with st.container():
     left, mid, right = st.columns([1, 1, 1])
     with left:
          if st.button("+ What is Verticai's end goal"):
               st.write("From anywhere in any country, Verticai wishes to give everyone a free mentor that can help them with their school work!")
     with mid:
          if st.button("+ Can Verticai answer any question?"):
               st.write("So far, Verticai is in training and can only answer a few questions from various Canadian textbooks like Pearson, Nelson, etc.")
     with right:
          if st.button("+ Does Verticai support cheating?"):
               st.write("No, Verticai implicitly supports good usage of education by giving everyone access to educational resources.")





with st.container():
     left, mid, right = st.columns([1, 1, 1])
     with mid:
          if st.button("+ Get Started"):
               subject = st.text_input("What is your subject?")
               grade = st.number_input("What is your grade?")
               country = st.text_input("What is your country?")



st.header("People from everywhere around the world don't have access to solid education")
st.subheader("We're here to solve that issue")




# Sign up for our early release
with st.form(key='my_form'):
     email = st.text_input('Email')
     name = st.text_input('Name')
     st.form_submit_button('Sign up')
