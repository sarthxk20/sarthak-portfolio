import streamlit as st

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
        "**Data Scientist | Python | SQL | Applied Machine Learning | Analytics & Visualization**"
    )
    st.markdown(
        "_Bridging data, intelligence, and action through meaningful insights._"
    )
    st.markdown("---")

def show_about():
    st.header("About Me")
    st.write(
        """
Hello! I'm Sarthak Shandilya, a Data Scientist with a strong focus on machine learning,
statistical modeling, and end-to-end data product development. I work on building scalable
data pipelines, developing predictive models, and translating analytical outputs into
decision-ready insights.

**Core Focus Areas:**
- Machine Learning and Predictive Modeling
- Statistical Analysis and Time-Series Forecasting
- Feature Engineering and Data Pipelines
- Interactive Data Applications and Dashboards (Streamlit)
"""
    )
    st.markdown("---")


def show_contact():
    st.header("Contact")
    st.write(
        """
 **Email:** [sarthakshandilya9@gmail.com](mailto:sarthakshandilya9@gmail.com)  
 **LinkedIn:** [linkedin.com/in/sarthxk20](https://linkedin.com/in/sarthxk20)  
 **GitHub:** [github.com/sarthxk20](https://github.com/sarthxk20)
"""
    )
    st.markdown("---")

def show_featured_project():
    st.header("Featured Projects")

    # -------------------------------
    # DemandIQ Project
    # -------------------------------
    st.subheader("DemandIQ - Retail Demand Forecasting & Risk Insights")

    st.write(
        """
A production-grade retail demand forecasting and decision support system built on
large-scale time-series data to support inventory planning and risk-aware decision-making.
"""
    )

    st.markdown("**Highlights:**")
    st.markdown(
        """
- Time-series forecasting system on 1M+ sales using Naive, ARIMA, SARIMA, and Prophet models  
- Forecast error reduction of ~60% using seasonality-aware approaches  
- Inventory planning ranges, demand risk estimation, and scenario simulation  
- Anomaly detection using statistical residual analysis  
- Optimized data pipeline using Parquet for scalable cloud deployment  
- Deployed interactive decision dashboard using Streamlit and Plotly  
"""
    )

    st.markdown("**Live App:** https://demandiq.streamlit.app")
    st.markdown("**GitHub:** https://github.com/sarthxk20/DemandIQ")

    st.markdown("---")

    # -------------------------------
    # SpaceX Project
    # -------------------------------
    st.subheader("SpaceX Launch Dashboard")

    st.write(
        """
A data-driven analytics dashboard exploring SpaceX launch performance and mission
outcomes using historical launch data and predictive modeling.
"""
    )

    st.markdown("**Highlights:**")
    st.markdown(
        """
- Automated data ingestion using the SpaceX API  
- Exploratory analysis of launch success trends
- Built a machine learning-based launch success predictor to estimate the probability of successful missions  
- Logistic regression model for launch success prediction  
- Interactive visualizations using Plotly  
- Deployed as a Streamlit application  
"""
    )
  
    st.markdown("**Live App:** https://spacex-launch-dashboard.streamlit.app")
    st.markdown("**GitHub:** https://github.com/sarthxk20/spacex-launch-dashboard")

    st.markdown("---")

    # -------------------------------
    # Resume Screening Project
    # -------------------------------
    st.subheader("Resume Screening System (ATS Simulation)")

    st.write(
        """
An NLP-based Applicant Tracking System (ATS) simulation designed to evaluate resume
relevance against job descriptions using semantic similarity and explainable scoring.
"""
    )

    st.markdown("**Highlights:**")
    st.markdown(
        """
- Resume-job matching using TF-IDF and BERT embeddings  
- Semantic similarity scoring for contextual relevance  
- Explainable skill gap and keyword coverage analysis  
- Reproducible inference and transparent evaluation logic  
- Deployed as an interactive Streamlit application  
"""
    )

    st.markdown("**Live App:** https://resume-screening-ai.streamlit.app")
    st.markdown("**GitHub:** https://github.com/sarthxk20/resume-screening-ai")

    st.markdown("---")


def show_why_hire():
    st.header("Why Hire Me?")
    st.write(
        """
I build end-to-end data science solutions that go beyond modeling - from data
ingestion and feature engineering to predictive modeling and production-ready
deployment. My work emphasizes interpretable machine learning, scalable data
pipelines, and translating complex analytical results into clear, actionable
insights that support real business decisions.
"""
    )
    st.markdown("---")

def show_tech_and_skills():
    st.header("Tech Stack & Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Tech Stack")
        st.markdown(
            """
- **Programming:** Python, SQL, R
- **Data Analysis:** Pandas, NumPy, Statsmodels  
- **Machine Learning:** Scikit-learn, Prophet  
- **Deep Learning:** TensorFlow, PyTorch (ANN, CNN, RNN, LSTM)  
- **NLP:** TF-IDF, BERT, Hugging Face  
- **Visualization:** Plotly, Matplotlib, Seaborn  
- **Data Apps & Deployment:** Streamlit, Streamlit Cloud  
- **Big Data & Tools:** Apache Spark, Hadoop  
- **BI & Reporting:** Tableau, Power BI  
- **Version Control & Dev Tools:** Git, GitHub, VS Code  
"""
        )

    with col2:
        st.subheader("Core Skills")
        st.markdown(
            """
- Data Cleaning, Preprocessing, and Validation  
- Exploratory Data Analysis and Statistical Insights  
- Feature Engineering and ETL Pipelines  
- Time-Series Forecasting and Predictive Modeling  
- NLP and Semantic Similarity Modeling  
- Model Evaluation and Performance Optimization  
- End-to-End ML Pipelines and Deployment  
- Business-Focused Analytics and Decision Support  
"""
        )

    st.markdown("---")

def show_certification():
    st.header("Certifications")

    st.markdown(
        """
**Applied Data Science Lab - WorldQuant University**  
- Applied machine learning techniques to real-world datasets  
- Focused on model evaluation, validation, and data-driven decision-making  
- Worked with unstructured data and databases such as MongoDB  

**Data Science Professional Certificate - IBM**  
- Completed an industry-aligned data science curriculum with hands-on labs and capstone projects  
- Covered Python, SQL, statistical analysis, machine learning, APIs, and data visualization  
- Built end-to-end data science workflows from data ingestion to model deployment  

**Machine Learning & AI with Python - HarvardX (edX)**  
- Implemented and evaluated supervised learning models in Python  
- Gained hands-on experience with ensemble methods including Bagging, Random Forests, Gradient Boosting, and AdaBoost  
- Developed an understanding of bias-variance trade-offs and metric-driven model selection  
"""
    )

    st.markdown("---")

def show_resume():
    st.header("Resume")

    st.write(
        """
Download my resume to learn more about my experience, projects, and technical background
in data science, machine learning, and analytics.
"""
    )

    with open("sarthak_shandilya_resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume (PDF)",
            data=file,
            file_name="Sarthak_Shandilya_Resume.pdf",
            mime="application/pdf",
        )

    st.markdown("---")


def show_personal():
    st.header("Personal")

    with st.expander("Why Data Science?"):
        st.write(
            """
I enjoy solving real-world problems using data - from uncovering hidden patterns
to building models that support better decisions. Data science lets me combine
analytical thinking with practical impact.
"""
        )

    with st.expander("Fun Fact"):
        st.write(
            """
I experiment with machine learning on my own datasets, including analyzing gameplay
and performance statistics to understand patterns and improve outcomes.
"""
        )

    st.markdown("---")


def show_footer():
    st.markdown(
        """
(c) 2026 Sarthak Shandilya  
Built with Python, Streamlit, and Plotly
"""
    )


# ---------- SIDEBAR NAV ----------
def main():
    set_page_config()

    st.sidebar.header("Navigate")

    page_map = {
        "All": None,
        "About Me": show_about,
        "Contact": show_contact,
        "Projects": show_featured_project,
        "Why Hire Me?": show_why_hire,
        "Tech Stack & Skills": show_tech_and_skills,
        "Certifications": show_certification,
        "Resume": show_resume,
        "Personal": show_personal,
    }

    choice = st.sidebar.radio("", list(page_map.keys()))

    show_header()

    if choice == "All":
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
        page_map[choice]()

if __name__ == "__main__":
    main()

