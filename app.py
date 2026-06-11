import streamlit as st

st.title("InternAI 🚀")

st.write("AI Internship and Placement Agent")

option = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Resume Analyzer",
        "Skill Gap Analysis",
        "Interview Coach",
        "Career Roadmap"
    ]
)

st.write(f"Selected: {option}")
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)
from agents.resume_agent import extract_text

if uploaded_file is not None:
    text = extract_text(uploaded_file)
    st.write(text)