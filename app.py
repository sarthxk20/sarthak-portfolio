import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ----------
def set_page_config():
    st.set_page_config(
        page_title="Sarthak Shandilya | Data Science Portfolio",
        layout="wide",
        initial_sidebar_state="auto",
    )

# ---------- GLOBAL CSS ----------
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

        a { color: var(--accent); }

        ul, ol, li { color: #ffffff !important; }
        ul li::marker { color: #ffffff !important; }

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

# ---------- SECTIONS ----------
def show_header():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>Sarthak Shandilya</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center; color:var(--muted);'>Data Scientist | Python | SQL | Machine Learning | NLP | IBM Certified</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:var(--muted);'><i>Bridging data, intelligence, and action through meaningful insights.</i></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def show_about():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>👋 About Me</h2>", unsafe_allow_html=True)
    st.write("""
    Hello! I’m **Sarthak Shandilya**, a Data Scientist skilled in **machine learning, statistical analysis**, and **end-to-end data application development**.
    I hold an **IBM Data Science Professional Certificate** and specialize in building scalable, data-driven solutions.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

def show_contact():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>📫 Contact</h2>", unsafe_allow_html=True)
    st.write("""
📧 **Email:** sarthakshandilya9@gmail.com  
💼 **LinkedIn:** https://linkedin.com/in/sarthxk20  
💻 **GitHub:** https://github.com/sarthxk20
    """)
    st.markdown("</div>", unsafe_allow_html=True)

def show_featured_project():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>🚀 Featured Project</h2>", unsafe_allow_html=True)
    st.subheader("SpaceX Launch Analysis Dashboard")

    col1, col2 = st.columns([1, 2])
    with col1:
        img = Image.open("spacex_dashboard.png")
        st.image(img, use_container_width=True)
    with col2:
        st.write("""
        - API-driven data ingestion and preprocessing  
        - Feature engineering and Logistic Regression modeling  
        - Interactive Plotly visualizations  
        - Deployed on Streamlit Cloud  
        """)
        st.markdown("🔗 https://spacex-launch-dashboard.streamlit.app")
        st.markdown("💻 https://github.com/sarthxk20/spacex-launch-dashboard")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- NEW PROJECT (ONLY ADDITION) ----------
def show_resume_screening_project():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>🧠 Resume Screening System (ATS Simulation)</h2>", unsafe_allow_html=True)
    st.write("""
    An AI-powered Applicant Tracking System (ATS) simulation that evaluates resumes
    against job descriptions using NLP and semantic similarity models.
    
    **Key Contributions:**
    - Implemented resume–job matching using TF-IDF and BERT embeddings  
    - Built skill gap and keyword coverage analysis  
    - Designed explainable hiring insights and confidence scoring  
    - Compared keyword-based vs semantic NLP approaches  
    """)
    st.markdown("💻 https://github.com/sarthxk20/resume-screening-ai")
    st.markdown("</div>", unsafe_allow_html=True)

def show_why_hire():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>Why Hire Me?</h2>", unsafe_allow_html=True)
    st.write("""
    I build end-to-end data solutions with a focus on clarity, explainability,
    and real-world impact — from raw data to deployed ML applications.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

def show_tech_and_skills():
    st.markdown("<div class='section-card'><h2>🧠 Tech Stack & Skills</h2></div>", unsafe_allow_html=True)
    st.markdown("""
- Python, SQL  
- Pandas, NumPy, scikit-learn  
- NLP: TF-IDF, BERT  
- Deep Learning: ANN, CNN, RNN, LSTM  
- Streamlit, Plotly  
    """)

def show_certification():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>🎓 Certification</h2>", unsafe_allow_html=True)
    st.write("IBM Data Science Professional Certificate")
    st.markdown("</div>", unsafe_allow_html=True)

def show_resume():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    with open("sarthak_shandilya_resume.pdf", "rb") as file:
        st.download_button("📥 Download Resume", file, "Sarthak_Shandilya_Resume.pdf")
    st.markdown("</div>", unsafe_allow_html=True)

def show_personal():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>💬 Personal</h2>", unsafe_allow_html=True)
    with st.expander("Why Data Science?"):
        st.write("I enjoy turning complex data into actionable insights.")
    with st.expander("Fun Fact"):
        st.write("I analyze my gameplay stats using ML for fun.")
    st.markdown("</div>", unsafe_allow_html=True)

def show_footer():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>© 2025 Sarthak Shandilya</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- MAIN ----------
def main():
    set_page_config()
    inject_custom_css()

    st.sidebar.markdown("<div class='sidebar-card'><strong>Navigate</strong></div>", unsafe_allow_html=True)

    pages = [
        "All",
        "About Me",
        "Contact",
        "Featured Project",
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
            "Featured Project": show_featured_project,
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
