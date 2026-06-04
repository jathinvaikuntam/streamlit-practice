import streamlit as st

st.title("Student Form")

name = st.text_input("Name")

age = st.number_input("Age",min_value=1)

course = st.selectbox(
    "Course",
    ["CSE", "ECE", "EEE", "Mechanical","AI/ML","Data Science"],
)

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)