import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("The Best Company")

content = """
AI startups often emerge from the intersection of technology, data, and entrepreneurship to address various 
industry challenges or create new opportunities by harnessing the power of AI. They may develop AI software, 
build AI-powered platforms, create AI algorithms, or design hardware optimized for AI processing
"""
st.write(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns([2, 2, 2])

df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        # name = row["first name"] + " " +row["last name"]
        # st.title(name)
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.text(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        # name = row["first name"] + " " + row["last name"]
        # st.title(name)
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.text(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        # name = row["first name"] + " " + row["last name"]
        # st.title(name)
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.text(row["role"])
        st.image("images/" + row["image"])
