import streamlit as st

# Title of the app
st.title("Enhanced Streamlit App")

# Add a sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

# Home page
if page == "Home":
    st.header("Welcome to the Enhanced Streamlit App!")
    st.write("This is an improved version of your first app.")
    
    # Add an input box
    name = st.text_input("What's your name?")
    
    # Display a greeting if a name is entered
    if name:
        st.write(f"Hello, {name}! Enjoy exploring the app.")

# About page
elif page == "About":
    st.header("About This App")
    st.write("This app is built using Streamlit. It's simple, interactive, and fun!")