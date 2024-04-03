import streamlit as st

st.set_page_config(layout="wide")

st.title("The Best Company")

content = """
AI startups often emerge from the intersection of technology, data, and entrepreneurship to address various 
industry challenges or create new opportunities by harnessing the power of AI. They may develop AI software, 
build AI-powered platforms, create AI algorithms, or design hardware optimized for AI processing
"""
st.write(content)

st.header("Our Team")

col1, col2, col3 = st.columns(3)
