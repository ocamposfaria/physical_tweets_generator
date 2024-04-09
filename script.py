import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import os
from config import *


st.markdown('## 📝 Gerador de tweet físico')

st.markdown('')

# streamlit input
tweet = st.text_input('Escreva seu tweet 👇', max_chars=175)

st.markdown('')
st.markdown('')

generate_image(tweet)


with open('images/output_image.jpg', "rb") as file:
    btn = st.download_button(
            label="Baixar tweet físico",
            data=file,
            file_name="tweet_físico.png"
          )
    
footer="""<style>
a:link , a:visited{
color: grey;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #0c0f14;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>desenvolvido por diversão por <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/ocamposfaria" target="_blank"> @ocamposfaria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
