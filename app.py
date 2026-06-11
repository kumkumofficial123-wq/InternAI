import streamlit as st
from agents.internship_agent import get_internships
from agents.roadmap_agent import skill_gap

st.set_page_config(
    page_title="InternAI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 InternAI")
st.write("AI Internship and Placement Agent")

option = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Resume Analyzer",
        "Internship Finder",
        "Interview Coach",
        "Skill Gap Analysis",
        "Career Roadmap"
    ]
)

# Resume Analyzer
if option == "Resume Analyzer":
    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:
        from agents.resume_agent import extract_text

        text = extract_text(uploaded_file)

        st.success("Resume Uploaded Successfully!")
        st.write(text[:2000])

# Internship Finder
elif option == "Internship Finder":
    st.header("💼 Internship Finder")

    df = get_internships()
    st.dataframe(df)

# Interview Coach
elif option == "Interview Coach":
    st.header("🎤 Interview Coach")

    role = st.text_input("Enter Job Role")

    if st.button("Generate Questions"):
        st.write(f"Interview questions for {role}")
        st.write("1. Tell me about yourself.")
        st.write("2. What are your strengths?")
        st.write("3. Why should we hire you?")

# Skill Gap Analysis
elif option == "Skill Gap Analysis":
    st.header("📊 Skill Gap Analysis")

    skills = st.text_input(
        "Enter Skills (comma separated)"
    )

    if st.button("Analyze"):
        user_skills = [s.strip() for s in skills.split(",")]
        missing = skill_gap(user_skills)

        st.write("Missing Skills:")
        st.write(missing)

# Career Roadmap
elif option == "Career Roadmap":
    st.header("🛣 Career Roadmap")

    goal = st.text_input("Enter Career Goal")

    if st.button("Generate Roadmap"):
        st.write(f"Roadmap for becoming a {goal}")
        st.write("Step 1: Learn Fundamentals")
        st.write("Step 2: Build Projects")
        st.write("Step 3: Apply for Internships")
        st.write("Step 4: Prepare for Interviews")