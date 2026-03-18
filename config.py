# config.py — Single source of truth for all portfolio content.
# Edit this file to update any text, links, or data in the portfolio.

# ── Personal Info ──────────────────────────────────────────────────────────────
PERSONAL = {
    "name": "Sarthak Shandilya",
    "title": "Data Scientist & Machine Learning Engineer",
    "tagline": "Building intelligent systems that transform data into measurable impact.",
    "bio": (
        "Data Scientist and Machine Learning Engineer with hands-on experience building "
        "end-to-end analytical and AI-powered systems — from data ingestion through to "
        "production deployment. I specialise in machine learning, NLP, and predictive "
        "modelling, and hold certifications from IBM, HarvardX, and WorldQuant University. "
        "I believe rigorous methodology and clear communication are what separate a good "
        "model from a useful one."
    ),
    "currently_learning": "MLflow, Docker, and building reproducible ML pipelines",
    "open_to": "Full-time Data Scientist or Machine Learning Engineer roles",
    "email": "sarthakshandilya9@gmail.com",
    "linkedin": "https://www.linkedin.com/in/sarthxk20",
    "github": "https://github.com/sarthxk20",
    "resume_url": "",  # Add Google Drive / Dropbox direct link here
    "location": "India",
}

# ── Headline Stats (shown in About strip) ─────────────────────────────────────
STATS = [
    {"value": "4+",  "label": "Projects Deployed"},
    {"value": "3",   "label": "Certifications"},
    {"value": "5+",  "label": "ML Algorithms Used"},
    {"value": "3+",  "label": "Visualization Tools"},
]

# ── Projects ──────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "title": "PortIQ — AI Portfolio Analyser",
        "tag": "Machine Learning · NLP · Financial Analysis · Streamlit",
        "problem": (
            "Retail investors lack accessible tools to objectively evaluate their "
            "portfolio composition, risk exposure, and alignment with financial goals."
        ),
        "approach": (
            "Built an AI-powered portfolio analysis engine that processes holdings data, "
            "applies ML-based risk scoring, and generates plain-language investment insights "
            "using NLP — making institutional-grade analysis accessible to individual investors."
        ),
        "result": (
            "A live, cloud-deployed Streamlit application that delivers personalised "
            "portfolio diagnostics, sector breakdowns, and actionable recommendations."
        ),
        "highlights": [
            "ML-based risk scoring across portfolio holdings",
            "NLP-generated plain-language investment insights",
            "Sector allocation and diversification analysis",
            "Deployed on Streamlit Cloud with real-time processing",
        ],
        "live_url": "https://portiq.streamlit.app/",
        "github_url": "https://github.com/sarthxk20/PortIQ",
        "badge_color": "#00E5FF",
    },
    {
        "title": "DemandIQ — Demand Forecasting Engine",
        "tag": "Time Series · Forecasting · Machine Learning · Streamlit",
        "problem": (
            "Businesses operating without accurate demand forecasts face chronic "
            "inventory imbalances — either excess stock or costly shortfalls."
        ),
        "approach": (
            "Developed a demand forecasting system leveraging time-series modelling "
            "and machine learning to predict future demand across product categories, "
            "with configurable forecast horizons and confidence intervals."
        ),
        "result": (
            "A deployed forecasting dashboard that allows businesses to simulate "
            "demand scenarios, visualise trends, and plan inventory with data-backed confidence."
        ),
        "highlights": [
            "Time-series forecasting with configurable horizons",
            "Confidence interval modelling for uncertainty quantification",
            "Interactive scenario simulation dashboard",
            "End-to-end pipeline from raw sales data to actionable forecast",
        ],
        "live_url": "https://demandiq.streamlit.app/",
        "github_url": "https://github.com/sarthxk20/DemandIQ",
        "badge_color": "#FFD166",
    },
    {
        "title": "SpaceX Launch Analysis Dashboard",
        "tag": "EDA · Predictive Modelling · Deployment",
        "problem": (
            "SpaceX's reusable rocket programme generates rich launch data, but no "
            "accessible tool existed to explore mission success patterns interactively."
        ),
        "approach": (
            "Integrated the SpaceX REST API with external datasets, performed "
            "feature engineering on launch parameters, and trained a Logistic Regression "
            "classifier to predict first-stage landing success."
        ),
        "result": (
            "A live Streamlit dashboard with Plotly visualisations enabling drill-down "
            "by orbit type, payload mass, and launch site."
        ),
        "highlights": [
            "Logistic Regression for launch success prediction",
            "Interactive Plotly + Seaborn visualisations",
            "Full pipeline: API collection to EDA to Modelling to Deployment",
        ],
        "live_url": "https://spacex-launch-dashboard.streamlit.app",
        "github_url": "https://github.com/sarthxk20/spacex-launch-dashboard",
        "badge_color": "#A78BFA",
    },
    {
        "title": "Resume Screening System (ATS Simulation)",
        "tag": "NLP · BERT · Semantic Similarity · Streamlit",
        "problem": (
            "Manual resume screening is slow and inconsistent, causing strong "
            "candidates to be overlooked due to keyword mismatch rather than lack of fit."
        ),
        "approach": (
            "Combined TF-IDF keyword matching with BERT-based semantic similarity "
            "to score resume-job description alignment, augmented with skill-gap "
            "analysis to surface missing competencies."
        ),
        "result": (
            "A cloud-deployed ATS simulation generating explainable screening reports "
            "that support faster, more consistent hiring decisions."
        ),
        "highlights": [
            "BERT semantic similarity + TF-IDF keyword matching",
            "Skill gap and keyword coverage analysis",
            "Explainable screening reports for transparent decision-making",
        ],
        "live_url": "https://resume-screening-ai.streamlit.app",
        "github_url": "https://github.com/sarthxk20/resume-screening-ai",
        "badge_color": "#34D399",
    },
]

# ── Tech Stack ────────────────────────────────────────────────────────────────
SKILLS = {
    "Languages": [
        {"name": "Python",  "level": 90},
        {"name": "SQL",     "level": 75},
    ],
    "ML & Data Science": [
        {"name": "Scikit-Learn",  "level": 85},
        {"name": "Pandas",        "level": 90},
        {"name": "NumPy",         "level": 85},
        {"name": "BERT / NLP",    "level": 70},
    ],
    "Visualisation": [
        {"name": "Plotly",   "level": 85},
        {"name": "Seaborn",  "level": 80},
        {"name": "Tableau",  "level": 65},
    ],
    "Deployment & Tools": [
        {"name": "Streamlit",    "level": 90},
        {"name": "GitHub",       "level": 80},
        {"name": "Google Colab", "level": 85},
        {"name": "VS Code",      "level": 85},
    ],
}

# ── Certifications ────────────────────────────────────────────────────────────
CERTIFICATIONS = [
    {
        "title": "Data Science Professional Certificate",
        "issuer": "IBM",
        "year": "2024",
        "description": (
            "10-course specialisation covering data analysis, machine learning, "
            "SQL, Python, and data visualisation with real-world capstone projects."
        ),
    },
    {
        "title": "Machine Learning & AI with Python",
        "issuer": "HarvardX (edX)",
        "year": "2024",
        "description": (
            "Graduate-level programme covering supervised and unsupervised learning, "
            "neural networks, and applied AI methods using Python."
        ),
    },
    {
        "title": "Applied Data Science Lab",
        "issuer": "WorldQuant University",
        "year": "2024",
        "description": (
            "Hands-on data science programme with project-based learning across "
            "data wrangling, statistical modelling, and applied machine learning."
        ),
    },
]

# ── Why Hire Me ───────────────────────────────────────────────────────────────
WHY_HIRE = [
    {
        "icon": "01",
        "heading": "Production-First Mindset",
        "body": (
            "Every project I build goes beyond the notebook — from data ingestion "
            "to a live, deployed application. I treat deployment as part of the "
            "work, not an afterthought."
        ),
    },
    {
        "icon": "02",
        "heading": "Breadth Across the ML Stack",
        "body": (
            "From time-series forecasting and NLP to classification and financial "
            "modelling, I have applied machine learning across diverse domains — "
            "with four deployed projects to demonstrate it."
        ),
    },
    {
        "icon": "03",
        "heading": "Insight Over Output",
        "body": (
            "I design for the decision-maker, not just the data team. My dashboards "
            "and reports are built to be immediately actionable for non-technical "
            "stakeholders — clarity is a feature, not a bonus."
        ),
    },
    {
        "icon": "04",
        "heading": "Verified, Multi-Institution Training",
        "body": (
            "Certified by IBM, HarvardX, and WorldQuant University — three programmes "
            "spanning core data science, graduate-level ML, and applied project work. "
            "Theory and practice in equal measure."
        ),
    },
]

# ── Personal ──────────────────────────────────────────────────────────────────
PERSONAL_SECTION = {
    "intro": (
        "Outside of work, I enjoy the kind of thinking that data science does not "
        "always allow for — whether that is getting absorbed in a film, following "
        "sport, reading, or losing track of time with a good game."
    ),
    "interests": [
        {"label": "Cinema & Films"},
        {"label": "Sports"},
        {"label": "Gaming"},
        {"label": "Reading"},
        {"label": "Music"},
        {"label": "Problem Solving"},
    ],
}
