import streamlit as st
st.title('Hello,Jathin! 👋')
st.write('This is my first Streamlit app.')
name=st.text_input('What is your name?')
if st.button('Greet me'):
    st.success(f'Welcome, {name}!')