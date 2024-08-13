import streamlit as st
import main
st.title("Sign Up!")

with st.form(key = "form"):
    reciever = st.text_input("Your Email Address")
    button = st.form_submit_button()
    if button:
        main.func(reciever)
        st.info("Signed Up!")