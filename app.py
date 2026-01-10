import streamlit as st
from PIL import Image

# ==================================================
# PAGE CONFIGURATION
# ==================================================
def set_page_config():
    st.set_page_config(
        page_title="Sarthak Shandilya | Data Science Portfolio",
        layout="wide",
        initial_sidebar_state="auto",
    )

# ==================================================
# GLOBAL STYLING (CSS)
# ==================================================
def inject_custom_css():
    st.markdown(
        """
        <style>
        :root {
            --bg: #0e1117;
            --card: #0f161a;
            --muted: #b9c7c6;
            --accent: #00bfae;
            --radius: 12px;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: var(--bg) !important;
            color: #e6eef0 !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial;
        }

        .block-container {
            padding: 1.5rem 2rem !important;
            max-width: 1200px;
            margin: auto;
        }

        h1, h2, h3, h4 {
            color: #e9fbfa;
            font-weight: 600;
        }

        h1 { font-size: 34px; }
        h2 { font-size: 22px; }
        h3 { font-size: 18px; }

        p, li {
            color: var(--muted);
            font-size: 15px;
            line-height: 1.6;
        }

        .section-card {
            background: rgba(255,255,255,0.02);
            border-radius: var(--radius);
            padding: 18px;
            box-shadow: 0 5px 18px rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.04);
            margin-bottom: 1.25rem;
        }

        a {
            color: var(--accent);
            text-decoration: none;
        }
        a:hover { text-decoration: underline; }

        ul, ol, li {
            color: #ffffff !important;
        }

        ul li::marker,
        ol li::marker {
            color: #ffffff !important;
        }

        [data-testid="stSidebar"] {
            background: rgba(255,255,255,0.02);
            border-right: 1px solid rgba(255,255,255,0.04);
        }

        .sidebar-card {
            padding: 10px 12px;
            border-radius: 10px;
            background: rgba(255,255,255,0.02);
            margin-bottom: 12px;
        }

        * { overflow-x: hidden !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ==================================================
# SECTIONS
# ==================================================
def show_header():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>Sarthak Shandilya</h1>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='text-align:center; color:var(--muted);'>"
        "Data Scientist | Python | SQL | Machine Learning | NLP | IBM Certified"
        "</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center; color:var(--muted);'><i>"
        "Bridging data, intelligence, and action through meaningful insights."
        "</i></p>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_about():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>About Me</h2>", unsafe_allow_html=True)
    st.write(
        """
I am a Data Scientist with experience building end-to-end machine learning and NLP systems.
I focus on transforming raw data into actionable insights through modeling, analysis,
and deployment-ready applications.

Core interests include applied machine learning, semantic text analysis,
and explainable AI systems.
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_contact():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>Contact</h2>", unsafe_allow_html=True)
    st.write(
        """
Email: sarthakshandilya9@gmail.com  
LinkedIn: https://linkedin.com/in/sarthxk20  
GitHub: https://github.com/sarthxk20
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# FEATURED PROJECTS
# ==================================================
def show_featured_projects():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>Featured Projects</h2>", unsafe_allow_html=True)

    # -------- SpaceX Project --------
    st.subheader("SpaceX Launch Analysis Dashboard")
    col1, col2 = st.columns([1, 2])

    with col1:
        img = Image.open("spacex_dashboard.png")
        st.image(img, caption="SpaceX Dashboard", use_container_width=True)

    with col2:
        st.write(
            """
A data-driven dashboard analyzing SpaceX launch data using Python,
EDA, and supervised machine learning.

Highlights:
- API-based data ingestion and preprocessing
- Feature engineering and Logistic Regression modeling
- Interactive visualizations with Plotly
- Deployed on Streamlit Cloud
            """
        )
        st.markdown("Live App: https://spacex-launch-dashboard.streamlit.app")
        st.markdown("GitHub: https://github.com/sarthxk20/spacex-launch-dashboard")

    st.markdown("---")

    # -------- Resume Screening Project --------
    st.subheader("Resume Screening System (ATS Simulation)")
    st.write(
        """
An AI-powered Applicant Tracking System (ATS) simulation that evaluates resumes
against job descriptions using NLP and semantic similarity techniques.

Highlights:
- Resume–job matching using TF-IDF and BERT embeddings
- Skill gap and keyword coverage analysis
- Explainable hiring decisions and confidence scoring
- Comparison of keyword-based vs semantic NLP approaches
        """
    )
    st.markdown("GitHub: https://github.com/sarthxk20/resume-screening-ai")

    st.markdown("</div>", unsafe_allow_html=True)

def show_tech_and_skills():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>Tech Stack & Skills</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
**Tech Stack**
- Python, SQL  
- Pandas, NumPy, scikit-learn  
- NLP: TF-IDF, BERT  
- Deep Learning: ANN, CNN, RNN, LSTM  
- Streamlit, Plotly  
            """
        )

    with col2:
        st.markdown(
            """
**Core Skills**
- Data Cleaning & Feature Engineering  
- Exploratory Data Analysis  
- Machine Learning Modeling  
- NLP & Semantic Similarity  
- End-to-End ML Pipelines  
            """
        )

    st.markdown("</div>", unsafe_allow_html=True)

def show_resume():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>Resume</h2>", unsafe_allow_html=True)
    with open("sarthak_shandilya_resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume",
            data=file,
            file_name="Sarthak_Shandilya_Resume.pdf",
            mime="application/pdf",
        )
    st.markdown("</div>", unsafe_allow_html=True)

def show_footer():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:gray;'>© 2025 Sarthak Shandilya</p>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# MAIN APP
# ==================================================
def main():
    set_page_config()
    inject_custom_css()

    st.sidebar.markdown("<div class='sidebar-card'><strong>Navigate</strong></div>", unsafe_allow_html=True)
    choice = st.sidebar.radio(
        "",
        ["All", "About Me", "Contact", "Projects", "Tech Stack & Skills", "Resume"],
    )

    if choice == "All":
        show_header()
        show_about()
        show_contact()
        show_featured_projects()
        show_tech_and_skills()
        show_resume()
        show_footer()
    elif choice == "Projects":
        show_header()
        show_featured_projects()
    else:
        show_header()
        {
            "About Me": show_about,
            "Contact": show_contact,
            "Tech Stack & Skills": show_tech_and_skills,
            "Resume": show_resume,
        }[choice]()
        show_footer()

if __name__ == "__main__":
    main()
