import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("Contact Us!..")

df = pd.read_csv('topics.csv')

# Create forms

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address:")
    # Select Box
    option = st.selectbox("How would you like to be contacted?", (df), index=None,
                          placeholder="Select contact method...", )
    st.write('You selected:', option)
    # Custom message box
    raw_message = st.text_area("Your message")
    message = f"""\
    Subject: New email from {user_email}

    From: {user_email}
    {raw_message}
    """
    # Submit Button
    button = st.form_submit_button("Submit")
    if button:
        st.info("Message send successfully")
