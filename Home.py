import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Alvin Chen")
    content = """
    As a Customer Support Engineer at actnano, a company that provides life-saving 
    nanocoating technology for electronics, I apply my technical support skills to 
    help grow and maintain customer satisfaction. 
    I have a Google Project Manager Career Certificate, 
    which demonstrates my ability to plan, execute, and deliver complex projects 
    using agile methodologies and tools. 
    
    With over 8 years of experience in the manufacturing and research industries, 
    I have successfully managed and supported multiple product lines, 
    such as Flexible Lighting Solutions, AC Modules, Robotics IR Module, and LiDAR. 
    I have led and collaborated with cross-functional teams to meet customer expectations 
    and win OEM and ODM projects. 
    
    I have also optimized the product quality and efficiency by improving the 
    material selection, design, and fabrication processes. 
    Additionally, I have a strong bilingual ability in Chinese and English, 
    which enables me to communicate effectively with global customers and partners.
    """
    st.info(content)

content2 = """
Below you can find my portfolio and the apps I have built in Python.
Please feel free to reach out to me if any questions.
"""
st.write(content2)

col3, empty_col2, col4 = st.columns([1.5, 0.3, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")