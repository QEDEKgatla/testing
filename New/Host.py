import streamlit as st

# Set page config without icon
st.set_page_config(page_title="Embedded HTML", layout="wide")

# Embed the local server content using iframe
st.markdown(
    '<iframe src="http://localhost:8000/T.html" width="100%" height="600" style="border:none;"></iframe>',
    unsafe_allow_html=True
)
