import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Sarthak Shandilya Portfolio", layout="wide")

# ---------- HEADER SECTION ----------
st.title("Sarthak Shandilya")
st.subheader("Aspiring Data Analyst | Python | Excel | Tableau | Streamlit | API Integration")

st.write("""
Hello! I'm a passionate data enthusiast with hands-on experience in data analysis, visualization, and dashboard development. 
I love working with Python, Excel, and tools like Streamlit and Tableau to turn raw data into meaningful insights.
""")

# ---------- SOCIAL LINKS ----------
st.markdown("**Email:** sarthakshandilya9@gmail.com")
st.markdown("**GitHub:** [github.com/sarthxk20](https://github.com/sarthxk20)")
st.markdown("**LinkedIn:** [linkedin.com/in/sarthxk20](https://linkedin.com/in/sarthxk20)")

# ---------- PROJECTS SECTION ----------
st.markdown("---")
st.header("Projects")

# Project 1: Sales Dashboard
st.subheader("1. Interactive Sales Dashboard")
st.write("""
Built a dynamic dashboard using Streamlit to visualize sales data. Features include:
- Regional and monthly performance metrics
- Filterable charts (Plotly)
- KPIs like total sales, sales by category
""")
st.markdown("**GitHub:** [View Project](https://github.com/sarthxk20/superstore-sales-dashboard)")

# Project 2: Weather App
st.subheader("2. Live Weather Forecast App")
st.write("""
Created a weather forecast app using Streamlit and OpenWeatherMap API. Features include:
- Real-time weather by city
- API integration and error handling
- Dynamic visuals (icons, temperature, wind, humidity)
""")
st.markdown("**GitHub:** [View Project](https://github.com/sarthxk20/weather-now)")

# ---------- ARTICLES / MINI BLOG SECTION ----------
st.markdown("---")
st.header("Articles & Insights")

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
I’m a self-driven and curious Data Analyst who turns raw data into meaningful insights.  
With hands-on experience in real-world projects using Python, Streamlit, and Tableau, I’ve built interactive dashboards and apps that showcase practical skills—not just theory.

I’m passionate about turning data into clear, actionable stories, continuously learning new tools, and solving real-world problems through analysis and visualization.  
I’m ready to bring energy, adaptability, and critical thinking to any data-focused team.
""")

# ---------- TECH STACK SECTION ----------
st.markdown("---")
st.header("Tech Stack")

st.write("""
Here's a snapshot of the tools and platforms I regularly use across my projects:

- **Programming Languages:** Python, SQL (basic)
- **Data Libraries:** Pandas, NumPy, Plotly, Seaborn, Matplotlib, Requests
- **App & Dashboard Tools:** Streamlit, Tableau
- **Development Tools:** Git & GitHub, Jupyter Notebook, VS Code
- **Deployment Platforms:** Streamlit Cloud, GitHub Pages, Google Colab
""")

# ---------- SKILLS SECTION ----------
st.markdown("---")
st.header("Skills")

st.write("""
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization & Storytelling
- Dashboard Development
- API Integration & JSON Handling
- Problem Solving & Critical Thinking
- Team Collaboration & Communication
""")

# ---------- RESUME SECTION ----------
st.markdown("---")
st.header("📄 My Resume")

st.write("Click below to download my resume as a PDF:")

with open("sarthak_shandilya_data_analyst_resume.pdf", "rb") as file:
    st.download_button(
        label="📥 Download Resume",
        data=file,
        file_name="Sarthak_Shandilya_Resume.pdf",
        mime="application/pdf"
    )

st.header("Get to Know Me")
with st.expander("🔍 Why data analysis?"):
    st.write("I enjoy finding patterns, asking questions, and turning messy data into something useful.")
with st.expander("🎮 Fun fact?"):
    st.write("I love strategy gaming and often track my own game stats!")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("*Built with ❤️ using Streamlit*")
