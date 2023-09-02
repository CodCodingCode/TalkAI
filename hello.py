import streamlit as st
import numpy as np
from PIL import Image
import streamlit as st




st.set_page_config(page_title="TalkAI", page_icon=":globe_with_meridians", layout="wide")
l, r, m = st.columns([1, 1, 1])
with r: 
     st.header('TalkAI')

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

g = st.slider("50", 0, 100, disabled=True)
for i in range(1, 50):
     g = g+1

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])

with tab1:
     st.write("hello")
with tab2:
     st.write("no")
                     


# Insert a chat message container.
with st.chat_message("user"):
     st.write("Hello 👋")
     st.line_chart(np.random.randn(300, 2))

# Display a chat input widget.
st.chat_input("Say something")

          

