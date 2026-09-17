import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Ankit Kumar | AI & Data Science Engineer | IIT Kanpur",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default Streamlit header and footer padding for a clean seamless experience
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    iframe {
        width: 100% !important;
        border: none !important;
    }
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Read index.html
current_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(current_dir, "index.html")

if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Read style.css and app.js to inline them for 100% reliable iframe rendering in Streamlit Cloud
    css_path = os.path.join(current_dir, "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
        html_content = html_content.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_content}</style>')

    js_path = os.path.join(current_dir, "app.js")
    if os.path.exists(js_path):
        with open(js_path, "r", encoding="utf-8") as f:
            js_content = f.read()
        html_content = html_content.replace('<script src="app.js"></script>', f'<script>{js_content}</script>')

    components.html(html_content, height=1400, scrolling=True)
else:
    st.error("index.html not found. Please ensure index.html exists in the repository root.")
