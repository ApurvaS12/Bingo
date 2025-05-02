import streamlit as st

# Config
st.set_page_config(page_title="Secret Soirée Bingo", layout="centered")

# Fonts and styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Love+Lace&display=swap');

    h1 {
        font-family: 'Abril Fatface', cursive;
        text-align: center;
        margin-bottom: 0.5em;
    }

    .bingo-button {
        font-family: 'Love Lace', cursive;
        font-style: italic;
        font-size: 13px;
        height: 100px;
        padding: 10px;
        white-space: normal;
        border-radius: 10px;
        width: 100
