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