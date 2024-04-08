import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def generate_image(tweet):

    # Define text and font
    text = tweet
    font_name = 'Bad'
    font_size = 400

    # carrega a imagem
    image = Image.open('images/img5.jpg')

    # pegando a fonte jojoba
    font_files = os.listdir('jojoba/')
    for file in font_files:
        if font_name.lower() in file.lower():    
            font_file = os.path.join('jojoba/', file)
    font = ImageFont.truetype(font_file, font_size)

    wrapped_text = textwrap.fill(text, width=25)

    # desenha na imagem
    draw = ImageDraw.Draw(image)
    draw.text((1, 1), wrapped_text, font=font, fill='blue')

    # salva a imagem e depois lê para jogar no streamlit
    output_path = 'images/output_image.jpg'
    image.save(output_path)
    output_image = Image.open(output_path)

    return st.image(output_image, use_column_width=True)