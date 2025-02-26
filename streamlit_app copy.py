import streamlit as st
st.set_page_config(
    page_title='Hello world',
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Hello world**'
        }
)
st.sidebar.title('Hello world')
st.sidebar.button("This is a button")
st.sidebar.button("I'm not sure how to route them.")
st.sidebar.button("Hi, I guess.")

st.title('Hello world')