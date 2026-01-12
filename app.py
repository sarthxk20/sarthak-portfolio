import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ----------
def set_page_config():
    st.set_page_config(
        page_title="Sarthak Shandilya | Data Science Portfolio",
        layout="wide",
        initial_sidebar_state="auto",
    )

# ---------- SECTIONS ----------
def show_header():
    st.markdown("## Sarthak Shandilya")
    st.markdown(
        "**Data Scientist | Python | SQL | Machine Learning | Data Analytics & Visualization | IBM Certified**"
    )
    st.markdown(
        "_Bridging data, intelligence, and action through meaningful insights._"
    )
    st.markdown("---")

def show_about():
    st.header("👋 About Me")
    st.write(
        """
Hello! I’m **Sarthak Shandilya**, a Data Scientist skilled in **machine learning,
statistical analysis**, and **end-to-end data application development**.
I hold an **IBM Data Science Professional Certificate** and specialize in building
scalable, data-driven solutions.

**Core Focus Areas:**
- Machine Learning Model Development
- Exploratory Data Analysis (EDA)
- Interactive Dashboards (Streamlit)
"""
    )
    st.markdown("---")

def show_contact():
    st.header("📫 Contact")
    st.write(
        """
📧 **Email:** [sarthakshandilya9@gmail.com](mailto:sarthakshandilya9@gmail.com)  
💼 **LinkedIn:** [linkedin.com/in/sarthxk20](https://linkedin.com/in/sarthxk20)  
💻 **GitHub:** [github.com/sarthxk20](https://github.com/sarthxk20)
"""
    )
    st.markdown("---")

def show_featured_project():
    st.header("🚀 Featured Project")
    st.subheader("SpaceX Launch Analysis Dashboard")

    col1, col2 = st.columns([1, 2])

    with col1:
        img = Image.open("spacex_dashboard.png")
        st.image(img, caption="SpaceX Dashboard", use_container_width=True)

    with col2:
        st.write(
            """
A data-driven dashboard exploring SpaceX launch trends using **Python, Plotly,
and Streamlit**.

**Highlights:**
- SpaceX API Integration
- Interactive Visualizations
- Logistic Regression for Success Prediction
- Streamlit Cloud Deployment
"""
        )
        st.markdown("**Live App:** https://spacex-launch-dashboard.streamlit.app")
        st.markdown("**GitHub:** https://github.com/sarthxk20/spacex-launch-dashboard")

    st.markdown("---")

def show_resume_screening_project():
    st.header("🚀 Featured Project")
    st.subheader("Resume Screening System (ATS Simulation)")

    col1, col2 = st.columns([1, 2])

    with col1:
        img = Image.open("resume.png")
        st.image(
            img,
            caption="Resume Screening System Interface",
            use_container_width=True
        )

    with col2:
        st.write(
            """
An AI-powered Applicant Tracking System (ATS) simulation that evaluates resumes
against job descriptions using NLP techniques and semantic similarity models.
"""
        )

        st.markdown("**Highlights:**")
        st.markdown(
            """
- Resume–Job Description matching using TF-IDF and BERT  
- Semantic similarity scoring for contextual relevance  
- Skill gap and keyword coverage analysis  
- Explainable screening decisions  
"""
        )

        st.markdown(
            "**Live App:** https://resume-screening-ai.streamlit.app"
        )
        st.markdown(
            "**GitHub:** https://github.com/sarthxk20/resume-screening-ai"
        )

    st.markdown("---")

def show_why_hire():
    st.header("Why Hire Me?")
    st.write(
        """
I deliver end-to-end data solutions — from raw data to fully deployed ML
applications. I focus on clarity, scalability, and real-world impact.
"""
    )
    st.markdown("---")

def show_tech_and_skills():
    st.header("🧠 Tech Stack & Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Tech Stack")
        st.markdown(
            """
- **Python**, **SQL**
- Pandas, NumPy, Sklearn, Matplotlib, Seaborn, Plotly
- TensorFlow, PyTorch (ANN, CNN, RNN, LSTM)
- NLP: BERT, GPT, HuggingFace, LangChain
- Big Data: Hadoop, Apache Spark
- Azure ML, Docker, Streamlit Cloud
- Tableau, Power BI
- Git, GitHub, VS Code
"""
        )

    with col2:
        st.subheader("Core Skills")
        st.markdown(
            """
- Data Cleaning & Preprocessing
- ETL & Feature Engineering
- EDA & Statistical Analysis
- End-to-End ML Pipelines
- Deep Learning & NLP
- Deployment & Dashboards
- Analytical Problem Solving
"""
        )

    st.markdown("---")

def show_certification():
    st.header("🎓 Certification")

    col1, col2 = st.columns([1, 3])

    with col1:
        cert = Image.open("certificate.png")
        st.image(cert, caption="IBM Certificate", use_container_width=True)

    with col2:
        st.write(
            """
**IBM Data Science Professional Certificate**  
Issued via Coursera  
Credential ID: 4UGBZJCVM3HZ
"""
        )

    st.markdown("---")

def show_resume():
    st.header("📄 Resume")

    with open("sarthak_shandilya_resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Sarthak_Shandilya_Resume.pdf",
            mime="application/pdf",
        )

    st.markdown("---")

def show_personal():
    st.header("💬 Personal")

    with st.expander("Why Data Science?"):
        st.write("I love turning complex data into meaningful insights.")

    with st.expander("Fun Fact"):
        st.write("I analyze my gameplay stats using ML for fun!")

    st.markdown("---")

def show_footer():
    st.markdown("© 2025 Sarthak Shandilya")

# ---------- SIDEBAR NAV ----------
def main():
    set_page_config()

    st.sidebar.header("Navigate")

    pages = [
        "All",
        "About Me",
        "Contact",
        "SpaceX Project",
        "Resume Screening Project",
        "Why Hire Me?",
        "Tech Stack & Skills",
        "Certification",
        "Resume",
        "Personal",
        "Footer",
    ]

    choice = st.sidebar.radio("", pages)

    if choice == "All":
        show_header()
        show_about()
        show_contact()
        show_featured_project()
        show_resume_screening_project()
        show_why_hire()
        show_tech_and_skills()
        show_certification()
        show_resume()
        show_personal()
        show_footer()
    else:
        show_header()
        {
            "About Me": show_about,
            "Contact": show_contact,
            "SpaceX Project": show_featured_project,
            "Resume Screening Project": show_resume_screening_project,
            "Why Hire Me?": show_why_hire,
            "Tech Stack & Skills": show_tech_and_skills,
            "Certification": show_certification,
            "Resume": show_resume,
            "Personal": show_personal,
            "Footer": show_footer,
        }[choice]()

if __name__ == "__main__":
    main()
