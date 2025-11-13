import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG & STYLE ----------
def set_page_config():
    st.set_page_config(page_title="Sarthak Shandilya | Data Science Portfolio", layout="wide")

def inject_custom_css():
    st.markdown("""
        <style>
            body { background-color: #0e1117; color: #e6e6e6; }
            .main { background-color: #0e1117; }
            h1, h2, h3, h4 {
                color: #00e0e0;
                text-shadow: 0 0 15px #00e0e0;
                animation: fadeIn 1.2s ease-in;
            }
            @keyframes fadeIn {
                0% { opacity: 0; transform: translateY(10px);}
                100% { opacity: 1; transform: translateY(0);}
            }
            hr {
                border: none;
                height: 2px;
                background: linear-gradient(to right, transparent, #00e0e0, transparent);
                margin: 40px 0;
            }
            a {
                color: #00e0e0;
                text-decoration: none;
                transition: color 0.3s ease, text-shadow 0.3s ease;
            }
            a:hover {
                color: #00ffff;
                text-shadow: 0 0 10px #00e0e0;
            }
            .cert-img {
                border-radius: 10px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .cert-img:hover {
                transform: scale(1.03);
                box-shadow: 0 0 20px rgba(0, 224, 224, 0.4);
            }
            p, li { font-size: 16px; line-height: 1.6; }
            html {
                scroll-behavior: smooth;
            }
        </style>
    """, unsafe_allow_html=True)

# ---------- SECTIONS ----------
def show_header():
    st.markdown("<h1 style='text-align:center;' id='about-me'>Sarthak Shandilya</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>Data Scientist | Python | SQL | Machine Learning | Data Analytics & Visualization | IBM Certified</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:18px; color:#9fdede;'><i>Bridging data, intelligence, and action through meaningful insights.</i></p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

def show_about():
    st.markdown("<h2 id='about-section'>👋 About Me</h2>", unsafe_allow_html=True)
    st.write("""
    Hello! I’m **Sarthak Shandilya**, a Data Scientist skilled in **machine learning, statistical analysis**, and **end-to-end data application development**.
    I hold an **IBM Data Science Professional Certificate** and specialize in building scalable, data-driven solutions that combine analytics, visualization, and predictive modeling.

    **Core Focus Areas:**
    - Developing and deploying machine learning models  
    - Performing exploratory data analysis (EDA) and hypothesis testing  
    - Building interactive dashboards and analytical tools using Streamlit  
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

def show_contact():
    st.markdown("<h2 id='contact'>📫 Get in Touch</h2>", unsafe_allow_html=True)
    st.write("""
        📧 **Email:** [sarthakshandilya9@gmail.com](mailto:sarthakshandilya9@gmail.com)  
        💼 **LinkedIn:** [linkedin.com/in/sarthxk20](https://linkedin.com/in/sarthxk20)  
        💻 **GitHub:** [github.com/sarthxk20](https://github.com/sarthxk20)
    """)
    st.markdown("<hr>", unsafe_allow_html=True)

def show_featured_project():
    st.markdown("<h2 id='featured-project'>🚀 Featured Project</h2>", unsafe_allow_html=True)
    st.subheader("SpaceX Launch Analysis Dashboard")
    col1, col2 = st.columns([1, 2])
    with col1:
        project_img = Image.open("spacex_dashboard.png")
        st.image(project_img, caption="SpaceX Launch Dashboard", use_container_width=True, output_format="JPEG")
    with col2:
        st.write("""
        A data-driven dashboard that explores SpaceX’s global launch history using **Python, Plotly, and Streamlit**.  
        This project combines exploratory data analysis and machine learning to reveal insights about launch success patterns and mission performance.

        **Technical Highlights:**
        - Integrated SpaceX API and merged datasets for launch history  
        - Cleaned, transformed, and visualized launch success trends  
        - Applied **Logistic Regression** for launch success prediction  
        - Built an interactive dashboard to explore **success rates, rockets, launchpads, and mission outcomes**  
        - Deployed via **Streamlit Cloud** for public accessibility  
        """)
        st.markdown("**🔗 Live App:** [spacex-launch-dashboard.streamlit.app](https://spacex-launch-dashboard.streamlit.app)")
        st.markdown("**💻 GitHub Repository:** [github.com/sarthxk20/spacex-launch-dashboard](https://github.com/sarthxk20/spacex-launch-dashboard)")
    st.markdown("<hr>", unsafe_allow_html=True)

    st.header("Articles & Insights")
    with st.expander("🧠 Behind the SpaceX Dashboard — Technical Breakdown"):
        st.write("""
            This project combined data engineering, analysis, visualization, and ML into a single workflow.
            I processed API data, performed statistical exploration, and built multiple plots to understand
            success trends across years, rockets, and launchpads.
            The machine learning component required building a clean feature space, handling categorical variables,
            and evaluating the model before deploying everything into an interactive Streamlit application.
        """)
    st.markdown("---")

def show_why_hire():
    st.markdown("<h2 id='why-hire-me'>Why Hire Me?</h2>", unsafe_allow_html=True)
    st.write("""
    I deliver complete data solutions — from collecting raw data to deploying ML-powered applications.  
    With experience across machine learning, analytics, and visualization tools,
    I build systems that make data understandable and actionable.

    I bring strong problem-solving skills, clean coding practices, and an ability to communicate insights clearly.
    If you need someone who can think analytically, work independently, and deliver real impact,
    I’m ready to contribute from day one.
    """)
    st.markdown("---")

def show_tech_and_skills():
    st.markdown("<h2 id='tech-stack-skills'>🧠 Tech Stack & 🧩 Core Skills</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tech Stack")
        st.write("""
        - **Programming Languages:** Python, SQL  
        - **Data Science Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Plotly  
        - **Machine Learning:** Supervised & Unsupervised Learning, Model Deployment, Ensemble Methods (Random Forest, XGBoost), Model Evaluation  
        - **Visualization Tools:** Streamlit, Tableau, Power BI  
        - **Development & Version Control:** Jupyter Notebook, VS Code, Git, GitHub  
        - **Deployment Platforms:** Streamlit Cloud, Google Colab, GitHub Pages  
        - **APIs & Automation:** REST APIs, BeautifulSoup, Selenium, Requests  
        """)
    with col2:
        st.subheader("Core Skills")
        st.write("""
        - Data Cleaning, Wrangling & Preprocessing  
        - Exploratory Data Analysis (EDA) & Statistical Modeling  
        - Machine Learning (Classification, Regression, Model Tuning)  
        - Data Visualization & Dashboard Design  
        - End-to-End ML Workflow & Deployment  
        - Problem Solving, Critical Thinking, and Communication  
        """)
    st.markdown("<hr>", unsafe_allow_html=True)

def show_certification():
    st.markdown("<h2 id='certification'>🎓 Certification</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        cert_img = Image.open("certificate.png")
        st.image(cert_img, caption="IBM Data Science Professional Certificate", use_container_width=True)
    with col2:
        st.markdown("""
            **IBM Data Science Professional Certificate**  
            *Issued by Coursera (Credential ID: 4UGBZJCVM3HZ)*  
            This program covered **Python, Data Analysis, SQL, Machine Learning, and Data Visualization**, culminating in a data-driven capstone project.  
            [🔗 View Certificate](https://www.coursera.org/account/accomplishments/professional-cert/4UGBZJCVM3HZ)
        """)
    st.markdown("<hr>", unsafe_allow_html=True)

def show_resume():
    st.markdown("<h2 id='resume'>📄 My Resume</h2>", unsafe_allow_html=True)
    st.write("Download my resume below:")
    with open("sarthak_shandilya_resume.pdf", "rb") as file:
        st.download_button(
            label="📥 Download Resume",
            data=file,
            file_name="Sarthak_Shandilya_Resume.pdf",
            mime="application/pdf"
        )
    st.markdown("---")

def show_personal():
    st.markdown("<h2 id='personal'>💬 Get to Know Me</h2>", unsafe_allow_html=True)
    with st.expander("🔍 Why Data Science & Machine Learning?"):
        st.write("""
            I’m driven by curiosity — I love turning complex data into clear insights.
            For me, data science is about blending analytical thinking with creativity to build models and tools that drive real-world impact.
        """)
    with st.expander("🎮 Fun Fact"):
        st.write("""
            I’m a strategy gaming enthusiast and often analyze my gameplay stats using data visualizations and predictive models —
            applying machine learning to my own hobbies is my favorite kind of experimentation!
        """)

def show_footer():
    st.markdown("<h2 id='footer'></h2>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>© 2025 Sarthak Shandilya — Powered by Streamlit</p>", unsafe_allow_html=True)

# ---------- SIDEBAR + SCROLLABLE MAIN PAGE ----------
def main():
    set_page_config()
    inject_custom_css()

    st.sidebar.title("Navigate")
    st.sidebar.markdown(
        """
        <style>
        .sidebar-content {font-size: 17px;}
        </style>
        """, unsafe_allow_html=True,
    )
    st.sidebar.markdown("[About Me](#about-section)", unsafe_allow_html=True)
    st.sidebar.markdown("[Contact](#contact)", unsafe_allow_html=True)
    st.sidebar.markdown("[Featured Project](#featured-project)", unsafe_allow_html=True)
    st.sidebar.markdown("[Why Hire Me?](#why-hire-me)", unsafe_allow_html=True)
    st.sidebar.markdown("[Tech Stack & Skills](#tech-stack-skills)", unsafe_allow_html=True)
    st.sidebar.markdown("[Certification](#certification)", unsafe_allow_html=True)
    st.sidebar.markdown("[Resume](#resume)", unsafe_allow_html=True)
    st.sidebar.markdown("[Personal](#personal)", unsafe_allow_html=True)
    st.sidebar.markdown("[Footer](#footer)", unsafe_allow_html=True)

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

if __name__ == "__main__":
    main()
