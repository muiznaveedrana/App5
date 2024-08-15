import streamlit as st
import main

st.title("Sign Up!")

with st.form(key="form"):
    receiver = st.text_input("Your Email Address")
    button = st.form_submit_button()

    if button:
        if receiver:  # Ensure that an email was entered
            main.func()
            with open("email.txt", "a") as file:  # Use append mode to avoid overwriting
                file.write(receiver + "\n")
            st.info("Signed Up!")
        else:
            st.warning("Please enter a valid email address.")
