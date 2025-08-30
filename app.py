import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Sarthak Shandilya Portfolio", layout="wide")

# ---------- HEADER SECTION ----------
st.title("Sarthak Shandilya")
st.subheader("Data Analyst | Aspiring Data Scientist | Building end-to-end solutions with Python, Machine Learning, and Streamlit")

st.write("""Hello! I’m Sarthak, a Data Analyst and Aspiring Data Scientist with hands-on experience in data analysis, machine learning, and dashboard development. I enjoy working with Python, SQL, Streamlit, and Tableau to transform raw data into actionable insights and interactive solutions.
""")

# ---------- SOCIAL LINKS ----------
st.markdown("**Email:** sarthakshandilya9@gmail.com")
st.markdown("**GitHub:** [github.com/sarthxk20](https://github.com/sarthxk20)")
st.markdown("**LinkedIn:** [linkedin.com/in/sarthxk20](https://linkedin.com/in/sarthxk20)")

# ---------- INTERNSHIP SECTION ----------
st.markdown("---")
st.header("Internships")

st.subheader("Data Analyst Intern – Evoastra")
st.write("""
Currently working as a Data Analyst Intern at **Evoastra**, contributing to a live web scraping and analytics project with a focus on **Exploratory Data Analysis (EDA)**.

**Key Responsibilities:**
- Conducting EDA on scraped datasets using **Pandas** and **Seaborn**
- Identifying patterns, trends, and outliers to support business insights
- Collaborating with the scraping team to ensure clean, analysis-ready data
- Contributing visual summaries to support dashboard development in **Streamlit**
""")


# ---------- PROJECTS SECTION ----------
st.markdown("---")
st.header("Projects")

# Project 1: Fraud Detection
st.subheader("1. Fraud Detection with Machine Learning")
st.write("""
Developed a machine learning model to detect fraudulent transactions. Features include:
- Data preprocessing, feature engineering, and EDA
- Classification models with evaluation (accuracy, precision, recall, F1-score)
- Interactive Streamlit app for real-time fraud prediction
""")
st.markdown("**Live App:** [fraud-detectionproject.streamlit.app](https://fraud-detectionproject.streamlit.app)")
st.markdown("**GitHub:** [View Project](https://github.com/sarthxk20/fraud-detection)")


# Project 2: Sales Dashboard
st.subheader("2. Interactive Sales Dashboard")
st.write("""
Built a dynamic dashboard using Streamlit to visualize sales data. Features include:
- Regional and monthly performance metrics
- Filterable charts (Plotly)
- KPIs like total sales, sales by category
""")
st.markdown("**Live App:** [sarthxk20-superstore-sales-dashboard.streamlit.app](https://sarthxk20-superstore-sales-dashboard.streamlit.app)")
st.markdown("**GitHub:** [View Project](https://github.com/sarthxk20/superstore-sales-dashboard)")

# Project 3: Weather App
st.subheader("3. Live Weather Forecast App")
st.write("""
Created a weather forecast app using Streamlit and OpenWeatherMap API. Features include:
- Real-time weather by city
- API integration and error handling
- Dynamic visuals (icons, temperature, wind, humidity)
""")
st.markdown("**Live App:** [weather-now-sarthxk20.streamlit.app](https://weather-now-sarthxk20.streamlit.app)")
st.markdown("**GitHub:** [View Project](https://github.com/sarthxk20/weather-now)")

# Project 4: Remote Python Job Dashboard
st.subheader("4. Remote Python Job Dashboard")
st.write("""
An interactive dashboard that visualizes remote Python job listings scraped from RemoteOK.
Features include:
- Real-time web scraping
- Filters by company, location, keyword
- Visuals: bar chart, word cloud, tech skills chart
- CSV download of filtered jobs
""")
st.markdown("**Live App:** [jobdash.streamlit.app](https://jobdash.streamlit.app)")
st.markdown("**GitHub:** [Remote Job Dashboard](https://github.com/sarthxk20/jobdash)")


# ---------- ARTICLES / MINI BLOG SECTION ----------
st.markdown("---")
st.header("Articles & Insights")

with st.expander("🧠 Building a Fraud Detection ML Model"):
    st.write("""
    I worked on a fraud detection project where the goal was to classify transactions as fraudulent or genuine.
    The main challenge was handling class imbalance since fraudulent cases were much fewer than normal ones.
    I applied techniques like feature engineering, exploratory data analysis (EDA), and trained classification models using Scikit-Learn.
    Evaluation metrics such as precision, recall, and F1-score were critical in measuring performance.
    Finally, I deployed the model as a Streamlit app for real-time fraud prediction.
    """)

with st.expander("📌 How I Built My Sales Dashboard"):
    st.write("""
    I used Streamlit, Pandas, and Plotly to build a responsive dashboard using Superstore sales data.
    The key challenge was cleaning and grouping data across regions and months.
    I learned how to use interactive filters, KPIs, and charts to tell a clear data story.
    """)

with st.expander("🌦️ Building a Weather Forecast App Using an API"):
    st.write("""
    This project helped me understand how to work with APIs in real time.
    I used the OpenWeatherMap API to fetch live data and handled errors like missing city names or API limits.
    Streamlit's layout tools made it easy to display everything cleanly with weather icons and themes.
    """)

# Optional: Add more later

st.markdown("---")
st.header("Why Hire Me?")

st.write("""
I’m a self-driven and curious Data Analyst | Aspiring Data Scientist who enjoys turning raw data into actionable insights.  
With hands-on experience in real-world projects, I’ve built and deployed solutions such as a fraud detection ML model, sales dashboard, web scraping app, and weather forecast tool using APIs.  

I combine skills in Python, SQL, Machine Learning, and visualization tools like Streamlit and Tableau to deliver clear, data-driven stories and decision-ready insights.  
Passionate about continuous learning, I bring adaptability, problem-solving, and critical thinking to every project and team I work with.
""")

# ---------- TECH STACK SECTION ----------
st.markdown("---")
st.header("Tech Stack")

st.write("""
Here's a snapshot of the tools and platforms I regularly use across my projects:

- Programming Languages: Python, SQL
- Data Libraries: Pandas, NumPy, Scikit-Learn, Plotly, Seaborn, Matplotlib, Requests
- App & Dashboard Tools: Streamlit, Tableau, Power BI
- Machine Learning: Scikit-Learn (classification, regression, model evaluation)
- Development Tools: Git, GitHub, Jupyter Notebook, VS Code
- Deployment Platforms: Streamlit Cloud, GitHub Pages, Google Colab
""")


# ---------- SKILLS SECTION ----------
st.markdown("---")
st.header("Skills")

st.write("""
- Data Cleaning, Wrangling & Preprocessing  
- Exploratory Data Analysis (EDA) & Statistical Analysis  
- Data Visualization & Storytelling (Seaborn, Plotly, Tableau)  
- Machine Learning (Classification, Regression, Model Evaluation)  
- Dashboard Development (Streamlit, Power BI, Tableau)  
- API Integration & Web Scraping  
- Problem Solving, Critical Thinking & Team Collaboration  
""")


# ---------- RESUME SECTION ----------
st.markdown("---")
st.header("📄 My Resume")

st.write("Click below to download my resume as a PDF:")

with open("sarthak_shandilya_resume.pdf", "rb") as file:
    st.download_button(
        label="📥 Download Resume",
        data=file,
        file_name="Sarthak_Shandilya_Resume.pdf",
        mime="application/pdf"
    )

st.header("Get to Know Me")

with st.expander("🔍 Why Data Analysis & Data Science?"):
    st.write("""
    I love uncovering patterns in data, asking meaningful questions, and turning messy datasets into actionable insights.  
    For me, data analysis is not just about numbers — it’s about solving real-world problems and telling impactful stories through data.
    """)

with st.expander("🎮 Fun fact"):
    st.write("""
    I’m a big fan of strategy gaming and often analyze my own gameplay stats to improve performance.  
    It’s like applying data analysis to gaming — insights that make the next move smarter!
    """)


# ---------- FOOTER ----------
st.markdown("---")
st.markdown("*Built with ❤️ using Streamlit*")



