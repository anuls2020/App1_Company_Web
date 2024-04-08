import streamlit as st
import pandas as pd
from send_email import send_mail

st.set_page_config(layout="wide")

st.header("Contact Us!..")

df = pd.read_csv('topics.csv')

# Create email sending forms

with st.form(key="email_forms"):
    user_mail_id = st.text_input("Your Email Address:")
    # Select Box
    option = st.selectbox("Choose an option", (df), index=None)
    st.write('You selected:', option)
    # Custom message box
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email regarding {option}

From: {user_mail_id}
{raw_message}
    """
    # Submit Button
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message)
        st.info("Message send successfully")
