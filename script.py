import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import os
from config import *


st.markdown('## 📝 Gerador de tweet físico')

st.markdown('')

# streamlit input
tweet = st.text_input('Escreva seu tweet 👇', max_chars=280)

st.markdown('')
st.markdown('')

generate_image(tweet)


with open('images\output_image.jpg', "rb") as file:
    btn = st.download_button(
            label="Baixar tweet físico",
            data=file,
            file_name="tweet_físico.png",
            mime="image/png"
          )
