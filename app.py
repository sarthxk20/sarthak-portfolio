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

        /* -------------------------
           Modern Minimal Theme
        --------------------------*/

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

        /* -------------------------
           Card Style Containers
        --------------------------*/

        .section-card {
            background: rgba(255,255,255,0.02);
            border-radius: var(--radius);
            padding: 18px;
            box-shadow: 0 5px 18px rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.04);
            margin-bottom: 1.25rem;
        }

        .accent-hr {
            height: 2px;
            background: var(--accent);
            margin: 18px 0;
            border-radius: 2px;
        }

        a {
            color: var(--accent);
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
        }

        /* -------------------------
           Sidebar
        --------------------------*/

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

        /* -------------------------
           Bullet visibility fix
        --------------------------*/

        ul, ol, li {
            color: #ffffff !important;
        }

        ul li::marker,
        ol li::marker {
            color: #ffffff !important;
        }

        /* -------------------------
           Responsive
        --------------------------*/

        @media (max-width: 600px) {
            .block-container { padding: 1rem !important; }
            h1 { font-size: 26px; }
            h2 { font-size: 20px; }
            h3 { font-size: 16px; }
            p, li { font-size: 14px; }
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
    st.markdown(
        "<h3 style='text-align:center; color:var(--muted);'>"
        "Data Scientist | Python | SQL | Machine Learning | Data Analytics & Visualization | IBM Certified"
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
    st.markdown("<h2>👋 About Me</h2>", unsafe_allow_html=True)
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
    st.markdown("</div>", unsafe_allow_html=True)

def show_contact():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>📫 Contact</h2>", unsafe_allow_html=True)
    st.write(
        """
📧 **Email:** [sarthakshandilya9@gmail.com](mailto:sarthakshandilya9@gmail.com)  
💼 **LinkedIn:** [linkedin.com/in/sarthxk20](https://linkedin.com/in/sarthxk20)  
💻 **GitHub:** [github.com/sarthxk20](https://github.com/sarthxk20)
"""
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_featured_project():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>🚀 Featured Project</h2>", unsafe_allow_html=True)
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
        st.markdown("**🔗 Live App:** https://spacex-launch-dashboard.streamlit.app")
        st.markdown("**💻 GitHub:** https://github.com/sarthxk20/spacex-launch-dashboard")

    st.markdown("</div>", unsafe_allow_html=True)

def show_why_hire():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>Why Hire Me?</h2>", unsafe_allow_html=True)
    st.write(
        """
I deliver end-to-end data solutions — from raw data to fully deployed ML
applications. I focus on clarity, scalability, and real-world impact.
"""
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_tech_and_skills():
    st.markdown("<div class='section-card'><h2>🧠 Tech Stack & Skills</h2></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
### Tech Stack
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
        st.markdown(
            """
### Core Skills
- Data Cleaning & Preprocessing
- ETL & Feature Engineering
- EDA & Statistical Analysis
- End-to-End ML Pipelines
- Deep Learning & NLP
- Deployment & Dashboards
- Analytical Problem Solving
"""
        )

def show_certification():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>🎓 Certification</h2>", unsafe_allow_html=True)

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

    st.markdown("</div>", unsafe_allow_html=True)

def show_resume():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>📄 Resume</h2>", unsafe_allow_html=True)

    with open("sarthak_shandilya_resume.pdf", "rb") as file:
        st.download_button(
            label="📥 Download Resume",
            data=file,
            file_name="Sarthak_Shandilya_Resume.pdf",
            mime="application/pdf",
        )

    st.markdown("</div>", unsafe_allow_html=True)

def show_personal():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown("<h2>💬 Personal</h2>", unsafe_allow_html=True)

    with st.expander("🔍 Why Data Science?"):
        st.write("I love turning complex data into meaningful insights.")

    with st.expander("🎮 Fun Fact"):
        st.write("I analyze my gameplay stats using ML for fun!")

    st.markdown("</div>", unsafe_allow_html=True)

def show_footer():
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:gray;'>© 2025 Sarthak Shandilya</p>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- SIDEBAR NAV ----------
def main():
    set_page_config()
    inject_custom_css()

    st.sidebar.markdown(
        "<div class='sidebar-card'><strong>Navigate</strong></div>",
        unsafe_allow_html=True,
    )

    pages = [
        "All",
        "About Me",
        "Contact",
        "Featured Project",
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
            "Why Hire Me?": show_why_hire,
            "Tech Stack & Skills": show_tech_and_skills,
            "Certification": show_certification,
            "Resume": show_resume,
            "Personal": show_personal,
            "Footer": show_footer,
        }[choice]()

if __name__ == "__main__":
    main()
