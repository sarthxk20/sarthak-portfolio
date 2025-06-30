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
st.markdown("**GitHub:** [View Project](https://github.com/sarthxk20)")

# Project 2: Weather App
st.subheader("2. Live Weather Forecast App")
st.write("""
Created a weather forecast app using Streamlit and OpenWeatherMap API. Features include:
- Real-time weather by city
- API integration and error handling
- Dynamic visuals (icons, temperature, wind, humidity)
""")
st.markdown("**GitHub:** [View Project](https://github.com/sarthxk20)")

# ---------- SKILLS SECTION ----------
st.markdown("---")
st.header("Skills")
st.write("""
- **Languages & Tools:** Python, Excel, VS Code, Tableau
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Plotly
- **Techniques:** Data Cleaning, Data Visualization, API Integration
- **Frameworks:** Streamlit
""")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("*Built with ❤️ using Streamlit*")
