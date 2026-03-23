# app.py — Sarthak Shandilya · Data Science & ML Portfolio
# Single-file Streamlit portfolio. Edit the CONTENT section below to update anything.

from __future__ import annotations


from collections.abc import Callable

import streamlit as st


# ══════════════════════════════════════════════════════════════════════════════
# CONTENT — Edit this section to update your portfolio
# ══════════════════════════════════════════════════════════════════════════════

PERSONAL = {
    "name": "Sarthak Shandilya",
    "title": "Data Scientist & Machine Learning Engineer",
    "tagline": "Building intelligent systems that transform data into measurable impact.",
    "bio": (
        "Data Scientist and Machine Learning Engineer with hands-on experience building "
        "end-to-end analytical and AI-powered systems — from data ingestion through to "
        "production deployment. I specialise in machine learning, NLP, and predictive "
        "modelling, and hold certifications from IBM, HarvardX, and WorldQuant University. "
        "I am particularly interested in roles at tech, fintech, and e-commerce companies "
        "where data and ML directly shape product decisions and business outcomes — whether "
        "that is at a high-growth startup or within an analytics team at scale."
    ),
    "currently_learning": "MLflow, Docker, and building reproducible ML pipelines",
    "open_to": "Data Scientist · ML Engineer · Analytics — tech, fintech, and e-commerce",
    "email": "sarthakshandilya9@gmail.com",
    "linkedin": "https://www.linkedin.com/in/sarthxk20",
    "github": "https://github.com/sarthxk20",
    # To add your resume: upload resume.pdf to your portfolio GitHub repo, then set this to:
    # "https://raw.githubusercontent.com/sarthxk20/<your-portfolio-repo>/main/resume.pdf"
    "location": "India",
}

STATS = [
    {"value": "9+",  "label": "Projects Deployed"},
    {"value": "3",   "label": "Certifications"},
    {"value": "27",  "label": "Features Engineered"},
    {"value": "0.97","label": "Best Model AUC"},
]

PROJECTS = [
    {
        "title": "PortIQ — AI Portfolio Analyser",
        "tag": "Machine Learning · NLP · Financial Analysis · Streamlit",
        "problem": (
            "Retail investors lack accessible tools to objectively evaluate portfolio "
            "composition, risk exposure, and alignment with financial goals."
        ),
        "approach": (
            "Built an ML pipeline over 1,200 data points across 180 companies, engineering "
            "27 features including pain scores, digital readiness, and deal-size potential. "
            "Trained a Random Forest classifier with 5-fold cross-validation for robust scoring."
        ),
        "result": (
            "Achieved AUC ~0.97 on the scoring model. Deployed a live Streamlit dashboard "
            "delivering portfolio diagnostics, sector breakdowns, and tiered prospect rankings — "
            "turning analysis that would take a financial analyst hours into an instant, "
            "data-backed decision."
        ),
        "highlights": [
            "Random Forest classifier · AUC ~0.97 (5-fold CV)",
            "27 engineered features across 180 companies",
            "TAM / SAM / SOM market sizing built into the pipeline",
            "Deployed on Streamlit Cloud with real-time scoring",
        ],
        "live_url": "https://portiq.streamlit.app/",
        "github_url": "https://github.com/sarthxk20/PortIQ",
        "badge_color": "#00E5FF",
    },
    {
        "title": "DemandIQ — Demand Forecasting Engine",
        "tag": "Time Series · Forecasting · Prophet · Streamlit",
        "problem": (
            "Businesses without accurate demand forecasts face chronic inventory "
            "imbalances — either excess stock tying up capital or costly shortfalls."
        ),
        "approach": (
            "Decomposed historical sales into trend, seasonality, and residual components. "
            "Evaluated multiple models — Prophet, Statsmodels, and Scikit-learn — selecting "
            "the best performer, then added confidence intervals and anomaly detection."
        ),
        "result": (
            "A deployed 14-day forecasting dashboard enabling scenario simulation and "
            "inventory planning — addressing a problem that costs retailers an estimated "
            "12% of annual revenue through overstock and stockouts."
        ),
        "highlights": [
            "14-day demand forecasts with confidence interval modelling",
            "Multi-model comparison: Prophet, Statsmodels, Scikit-learn",
            "Anomaly detection via residual analysis",
            "Scenario simulation with real-time inventory impact",
        ],
        "live_url": "https://demandiq.streamlit.app/",
        "github_url": "https://github.com/sarthxk20/DemandIQ",
        "badge_color": "#FFD166",
    },
    {
        "title": "SpaceX Launch Analysis Dashboard",
        "tag": "EDA · Logistic Regression · Plotly · Streamlit",
        "problem": (
            "SpaceX's reusable rocket programme generates rich launch data, but no "
            "accessible tool existed to explore mission success patterns interactively."
        ),
        "approach": (
            "Collected data via the SpaceX REST API and web scraping across 4 structured "
            "notebooks — covering data wrangling, EDA, visualisation, and predictive "
            "modelling. Trained a Logistic Regression classifier on launch parameters."
        ),
        "result": (
            "An interactive Streamlit dashboard with a live ML-powered success predictor — "
            "demonstrating how predictive modelling can surface actionable patterns from "
            "complex, multi-source datasets that no manual analysis could replicate at scale."
        ),
        "highlights": [
            "Logistic Regression launch success predictor",
            "End-to-end pipeline across 4 structured notebooks",
            "SpaceX REST API + web scraping for data collection",
            "Interactive feature importance and mission analytics",
        ],
        "live_url": "https://spacex-launch-dashboard.streamlit.app",
        "github_url": "https://github.com/sarthxk20/spacex-launch-dashboard",
        "badge_color": "#A78BFA",
    },
]

SKILLS = {
    "Languages": [
        {"name": "Python", "level": 90},
        {"name": "SQL",    "level": 75},
    ],
    "ML & Data Science": [
        {"name": "Scikit-Learn", "level": 85},
        {"name": "Pandas",       "level": 90},
        {"name": "NumPy",        "level": 85},
        {"name": "BERT / NLP",   "level": 70},
    ],
    "Visualisation": [
        {"name": "Plotly",  "level": 85},
        {"name": "Seaborn", "level": 80},
        {"name": "Tableau", "level": 65},
    ],
    "Deployment & Tools": [
        {"name": "Streamlit",    "level": 90},
        {"name": "GitHub",       "level": 80},
        {"name": "Google Colab", "level": 85},
        {"name": "VS Code",      "level": 85},
    ],
}

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
            "with three deployed projects to demonstrate it."
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


# ══════════════════════════════════════════════════════════════════════════════
# STYLES
# ══════════════════════════════════════════════════════════════════════════════

def load_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600;700&display=swap');

        :root {
            --bg:      #0B0F1A;
            --surface: #111827;
            --border:  #1E2A3A;
            --accent:  #00E5FF;
            --gold:    #FFD166;
            --text:    #E2E8F0;
            --muted:   #64748B;
            --mono:    'Space Mono', monospace;
            --sans:    'DM Sans', sans-serif;
            --radius:  12px;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: var(--bg) !important;
            color: var(--text) !important;
            font-family: var(--sans) !important;
        }

        #MainMenu, footer, header { visibility: hidden; }
        [data-testid="stToolbar"] { display: none; }
        .block-container { padding: 2rem 3rem !important; max-width: 1100px; }

        [data-testid="stSidebar"] {
            background: var(--surface) !important;
            border-right: 1px solid var(--border) !important;
        }
        [data-testid="stSidebar"] * { color: var(--text) !important; }
        [data-testid="stSidebar"] [data-testid="stRadio"] label { cursor: pointer; }
        /* Override red radio dot to cyan */
        [data-testid="stSidebar"] input[type="radio"]:checked + div,
        [data-testid="stSidebar"] input[type="radio"]:checked + div > div { color: var(--accent) !important; }
        [data-testid="stSidebar"] [aria-checked="true"] { color: var(--accent) !important; }
        div[data-baseweb="radio"] > label > div:first-child { border-color: var(--accent) !important; }
        div[data-baseweb="radio"] > label > div:first-child div { background: var(--accent) !important; }
        .nav-header {
            font-family: var(--mono);
            font-size: 0.7rem;
            letter-spacing: 0.15em;
            color: var(--accent) !important;
            text-transform: uppercase;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border);
        }

        .section-label { font-family: var(--mono); font-size: 0.65rem; letter-spacing: 0.2em; color: var(--accent); text-transform: uppercase; margin-bottom: 0.4rem; }
        .section-title { font-size: 1.9rem; font-weight: 700; color: var(--text); margin-bottom: 1.5rem; line-height: 1.2; }
        .divider { border: none; border-top: 1px solid var(--border); margin: 2.5rem 0; }
        a { color: var(--accent); text-decoration: none; }
        a:hover { text-decoration: underline; }

        .hero-wrap { padding: 3.5rem 0 2rem; }
        .hero-mono { font-family: var(--mono); font-size: 0.75rem; color: var(--accent); letter-spacing: 0.12em; margin-bottom: 1rem; }
        .hero-name { font-size: 3.5rem; font-weight: 700; line-height: 1.05; color: var(--text); margin-bottom: 0.5rem; }
        .hero-name span { color: var(--accent); }
        .hero-title { font-family: var(--mono); font-size: 1rem; color: var(--muted); margin-bottom: 1.2rem; }
        .hero-tagline { font-size: 1.3rem; font-weight: 300; color: var(--text); max-width: 540px; line-height: 1.6; margin-bottom: 2rem; border-left: 3px solid var(--accent); padding-left: 1rem; }
        .hero-badges { display: flex; gap: 0.75rem; flex-wrap: wrap; }
        .badge { font-family: var(--mono); font-size: 0.7rem; padding: 0.35rem 0.85rem; border-radius: 999px; letter-spacing: 0.05em; }
        .badge-outline { border: 1px solid var(--accent); color: var(--accent); }
        .badge-fill { background: var(--accent); color: var(--bg); font-weight: 700; }
        .hero-cta { display: flex; gap: 1rem; margin-top: 1.8rem; flex-wrap: wrap; }
        .cta-btn { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.65rem 1.4rem; border-radius: var(--radius); font-family: var(--mono); font-size: 0.78rem; font-weight: 700; letter-spacing: 0.05em; cursor: pointer; transition: all 0.2s ease; text-decoration: none !important; }
        .cta-primary { background: var(--accent); color: var(--bg) !important; border: 2px solid var(--accent); }
        .cta-primary:hover { background: transparent; color: var(--accent) !important; }
        .cta-secondary { background: transparent; color: var(--text) !important; border: 2px solid var(--border); }
        .cta-secondary:hover { border-color: var(--accent); color: var(--accent) !important; }

        .stats-wrap { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--border); border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; margin: 2rem 0; }
        .stat-cell { background: var(--surface); padding: 1.2rem 1.5rem; text-align: center; }
        .stat-value { font-family: var(--mono); font-size: 1.8rem; font-weight: 700; color: var(--accent); line-height: 1; }
        .stat-label { font-size: 0.75rem; color: var(--muted); margin-top: 0.3rem; text-transform: uppercase; letter-spacing: 0.08em; }

        .project-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 2rem; margin-bottom: 1.5rem; transition: border-color 0.2s ease; position: relative; overflow: hidden; }
        .project-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, var(--accent-color, #00E5FF), transparent); }
        .project-card:hover { border-color: var(--accent); }
        .project-title { font-size: 1.3rem; font-weight: 700; color: var(--text); margin-bottom: 0.2rem; }
        .project-tag { font-family: var(--mono); font-size: 0.65rem; color: var(--muted); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.2rem; }
        .psa-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin: 1.2rem 0; }
        .psa-block { background: rgba(0,229,255,0.04); border: 1px solid var(--border); border-radius: 8px; padding: 0.9rem 1rem; }
        .psa-label { font-family: var(--mono); font-size: 0.6rem; color: var(--accent); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 0.4rem; }
        .psa-text { font-size: 0.85rem; color: var(--text); line-height: 1.5; }
        .project-highlights { margin: 1rem 0; padding: 0; list-style: none; }
        .project-highlights li { font-size: 0.82rem; color: var(--muted); padding: 0.2rem 0 0.2rem 1.2rem; position: relative; }
        .project-highlights li::before { content: '▸'; position: absolute; left: 0; color: var(--accent); }
        .project-links { display: flex; gap: 0.75rem; margin-top: 1.2rem; flex-wrap: wrap; }
        .project-link { display: inline-flex; align-items: center; font-family: var(--mono); font-size: 0.7rem; padding: 0.4rem 0.9rem; border-radius: 6px; border: 1px solid var(--border); color: var(--text) !important; transition: all 0.15s ease; }
        .project-link:hover { border-color: var(--accent); color: var(--accent) !important; text-decoration: none !important; }

        .skills-group { margin-bottom: 2rem; }
        .skills-group-title { font-family: var(--mono); font-size: 0.7rem; color: var(--gold); text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 0.8rem; }
        .skill-row { display: flex; align-items: center; gap: 1rem; margin-bottom: 0.65rem; }
        .skill-name { font-size: 0.85rem; color: var(--text); width: 140px; flex-shrink: 0; }
        .skill-bar-bg { flex: 1; height: 6px; background: var(--border); border-radius: 999px; overflow: hidden; }
        .skill-bar-fill { height: 100%; border-radius: 999px; background: linear-gradient(90deg, var(--accent), var(--gold)); }
        .skill-pct { font-family: var(--mono); font-size: 0.65rem; color: var(--muted); width: 32px; text-align: right; flex-shrink: 0; }

        .cert-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.5rem; margin-bottom: 1rem; }
        .cert-title { font-size: 1rem; font-weight: 600; color: var(--text); margin-bottom: 0.2rem; }
        .cert-meta { font-family: var(--mono); font-size: 0.65rem; color: var(--muted); margin-bottom: 0.5rem; }
        .cert-desc { font-size: 0.83rem; color: var(--muted); line-height: 1.5; }

        .why-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; }
        .why-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 1.4rem; transition: border-color 0.2s; }
        .why-card:hover { border-color: var(--accent); }
        .why-icon { font-family: var(--mono); font-size: 0.65rem; color: var(--accent); letter-spacing: 0.1em; margin-bottom: 0.6rem; }
        .why-heading { font-weight: 600; font-size: 0.95rem; color: var(--text); margin-bottom: 0.4rem; }
        .why-body { font-size: 0.82rem; color: var(--muted); line-height: 1.6; }

        .contact-grid { display: flex; flex-direction: column; gap: 0.75rem; max-width: 480px; }
        .contact-row { display: flex; align-items: center; gap: 1rem; background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 0.9rem 1.2rem; transition: border-color 0.2s; text-decoration: none !important; }
        .contact-row:hover { border-color: var(--accent); }
        .contact-label { font-family: var(--mono); font-size: 0.65rem; color: var(--muted); }
        .contact-value { font-size: 0.9rem; color: var(--text); }

        .interests-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.75rem; margin-top: 1.5rem; }
        .interest-chip { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius); padding: 0.9rem 1rem; text-align: center; font-size: 0.85rem; color: var(--text); transition: border-color 0.2s; font-family: var(--mono); letter-spacing: 0.04em; }
        .interest-chip:hover { border-color: var(--gold); }

        .footer { text-align: center; padding: 2rem 0 1rem; font-family: var(--mono); font-size: 0.65rem; color: var(--muted); border-top: 1px solid var(--border); margin-top: 3rem; letter-spacing: 0.08em; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════════════════════
# RENDER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def render_header() -> None:
    p = PERSONAL
    st.markdown(
        f"""
        <div class="hero-wrap">
            <div class="hero-mono">// PORTFOLIO · DATA SCIENCE</div>
            <div class="hero-name">{p["name"].split()[0]} <span>{p["name"].split()[1]}</span></div>
            <div class="hero-title">_{p["title"]}</div>
            <div class="hero-tagline">{p["tagline"]}</div>
            <div class="hero-badges">
                <span class="badge badge-fill">IBM Certified</span>
                <span class="badge badge-fill" style="background:var(--gold);color:var(--bg);">HarvardX</span>
                <span class="badge badge-fill" style="background:#A78BFA;color:var(--bg);">WorldQuant</span>
                <span class="badge badge-outline">{p["location"]}</span>
                <span class="badge badge-outline">Open to Work</span>
            </div>
            <div style="font-family:var(--mono);font-size:0.72rem;color:var(--muted);margin-top:1rem;letter-spacing:0.04em;">
                {p["email"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Use st.link_button for CTA buttons — avoids Streamlit HTML interception issues
    # and correctly handles mailto: links
    cols = st.columns([1, 1, 4])
    with cols[0]:
        st.link_button("GitHub", p["github"], use_container_width=True)
    with cols[1]:
        st.link_button("LinkedIn", p["linkedin"], use_container_width=True)
    st.markdown('<hr class="divider" />', unsafe_allow_html=True)


def render_about() -> None:
    stats_html = "".join(
        f'<div class="stat-cell"><div class="stat-value">{s["value"]}</div><div class="stat-label">{s["label"]}</div></div>'
        for s in STATS
    )
    st.markdown(
        f"""
        <div class="section-label">// 01 · ABOUT</div>
        <div class="section-title">Who I Am</div>
        <p style="font-size:1rem;line-height:1.75;color:var(--text);max-width:680px;margin-bottom:1.5rem;">{PERSONAL["bio"]}</p>
        <p style="font-size:0.85rem;color:var(--muted);font-family:var(--mono);margin-bottom:1.5rem;">
            Currently learning: {PERSONAL["currently_learning"]}<br/>
            Seeking: {PERSONAL["open_to"]}
        </p>
        <div class="stats-wrap">{stats_html}</div>
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


def render_projects() -> None:
    # Section header
    st.markdown(
        '<div class="section-label">// 02 · WORK</div><div class="section-title">Projects</div>',
        unsafe_allow_html=True,
    )
    # Each card in its own st.markdown call to avoid Streamlit's HTML truncation limit
    for p in PROJECTS:
        highlights = "".join(f"<li>{h}</li>" for h in p["highlights"])
        st.markdown(
            f"""
            <div class="project-card" style="--accent-color:{p['badge_color']}">
                <div class="project-title">{p["title"]}</div>
                <div class="project-tag">{p["tag"]}</div>
                <div class="psa-grid">
                    <div class="psa-block"><div class="psa-label">Problem</div><div class="psa-text">{p["problem"]}</div></div>
                    <div class="psa-block"><div class="psa-label">Approach</div><div class="psa-text">{p["approach"]}</div></div>
                    <div class="psa-block"><div class="psa-label">Result</div><div class="psa-text">{p["result"]}</div></div>
                </div>
                <ul class="project-highlights">{highlights}</ul>
                <div class="project-links">
                    <a class="project-link" href="{p['live_url']}" target="_blank">Live App</a>
                    <a class="project-link" href="{p['github_url']}" target="_blank">GitHub</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('<hr class="divider" />', unsafe_allow_html=True)


def render_skills() -> None:
    groups_html = ""
    for group, items in SKILLS.items():
        rows = "".join(
            f'<div class="skill-row"><div class="skill-name">{s["name"]}</div>'
            f'<div class="skill-bar-bg"><div class="skill-bar-fill" style="width:{s["level"]}%"></div></div>'
            f'<div class="skill-pct">{s["level"]}%</div></div>'
            for s in items
        )
        groups_html += f'<div class="skills-group"><div class="skills-group-title">{group}</div>{rows}</div>'
    st.markdown(
        f'<div class="section-label">// 03 · STACK</div><div class="section-title">Tech Stack</div>{groups_html}<hr class="divider" />',
        unsafe_allow_html=True,
    )


def render_certifications() -> None:
    cards_html = "".join(
        f'<div class="cert-card"><div class="cert-title">{c["title"]}</div>'
        f'<div class="cert-meta">{c["issuer"]} · {c["year"]}</div>'
        f'<div class="cert-desc">{c["description"]}</div></div>'
        for c in CERTIFICATIONS
    )
    st.markdown(
        f'<div class="section-label">// 04 · CREDENTIALS</div><div class="section-title">Certifications</div>{cards_html}<hr class="divider" />',
        unsafe_allow_html=True,
    )


def render_why_hire() -> None:
    cards_html = "".join(
        f'<div class="why-card"><div class="why-icon">{w["icon"]}</div>'
        f'<div class="why-heading">{w["heading"]}</div><div class="why-body">{w["body"]}</div></div>'
        for w in WHY_HIRE
    )
    st.markdown(
        f'<div class="section-label">// 05 · VALUE</div><div class="section-title">Why Hire Me?</div>'
        f'<div class="why-grid">{cards_html}</div><hr class="divider" />',
        unsafe_allow_html=True,
    )


def render_resume() -> None:
    st.markdown(
        '<div class="section-label">// 06 · RESUME</div>'
        '<div class="section-title">Resume</div>'
        '<p style="color:var(--muted);font-size:0.9rem;margin-bottom:1.5rem;">'
        "A full summary of my experience, projects, skills, and certifications.</p>",
        unsafe_allow_html=True,
    )
    try:
        with open("resume.pdf", "rb") as f:
            st.download_button(
                label="Download Resume (PDF)",
                data=f.read(),
                file_name="Sarthak_Shandilya_Resume.pdf",
                mime="application/pdf",
            )
    except FileNotFoundError:
        st.markdown(
            '<p style="color:var(--muted);font-family:var(--mono);font-size:0.78rem;">'
            "resume.pdf not found. Make sure it is in the same folder as app.py.</p>",
            unsafe_allow_html=True,
        )
    st.markdown('<hr class="divider" />', unsafe_allow_html=True)


def render_contact() -> None:
    p = PERSONAL
    st.markdown(
        f"""
        <div class="section-label">// 07 · CONTACT</div>
        <div class="section-title">Get in Touch</div>
        <p style="color:var(--muted);font-size:0.9rem;margin-bottom:1.5rem;max-width:480px;">
            Open to full-time roles, collaborations, and interesting conversations.
            The best way to reach me is via email.
        </p>
        <div class="contact-grid">
            <a class="contact-row" href="mailto:{p['email']}">
                <div><div class="contact-label">EMAIL</div><div class="contact-value">{p['email']}</div></div>
            </a>
            <a class="contact-row" href="{p['linkedin']}" target="_blank">
                <div><div class="contact-label">LINKEDIN</div><div class="contact-value">linkedin.com/in/sarthxk20</div></div>
            </a>
            <a class="contact-row" href="{p['github']}" target="_blank">
                <div><div class="contact-label">GITHUB</div><div class="contact-value">github.com/sarthxk20</div></div>
            </a>
        </div>
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


def render_personal() -> None:
    ps = PERSONAL_SECTION
    chips = "".join(f'<div class="interest-chip">{i["label"]}</div>' for i in ps["interests"])
    st.markdown(
        f"""
        <div class="section-label">// 08 · PERSONAL</div>
        <div class="section-title">Beyond the Data</div>
        <p style="font-size:0.95rem;color:var(--text);max-width:600px;line-height:1.7;">{ps["intro"]}</p>
        <div class="interests-grid">{chips}</div>
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    p = PERSONAL
    st.markdown(
        f'<div class="footer">© 2026 {p["name"]} · Built with Streamlit · '
        f'<a href="{p["github"]}" target="_blank">View Source</a></div>',
        unsafe_allow_html=True,
    )


# ══════════════════════════════════════════════════════════════════════════════
# ROUTING
# ══════════════════════════════════════════════════════════════════════════════

PAGES: dict[str, Callable[[], None] | None] = {
    "All":            None,
    "About Me":       render_about,
    "Projects":       render_projects,
    "Tech Stack":     render_skills,
    "Certifications": render_certifications,
    "Why Hire Me?":   render_why_hire,
    "Resume":         render_resume,
    "Contact":        render_contact,
    "Personal":       render_personal,
}


def main() -> None:
    st.set_page_config(
        page_title="Sarthak Shandilya | Data Scientist & ML Engineer",
        page_icon="🔬",
        layout="wide",
        initial_sidebar_state="auto",
    )
    load_css()

    st.sidebar.markdown('<div class="nav-header">// NAVIGATE</div>', unsafe_allow_html=True)
    choice = st.sidebar.radio("Navigation", list(PAGES.keys()), label_visibility="collapsed")

    render_header()

    if choice == "All":
        for fn in PAGES.values():
            if fn is not None:
                fn()
    else:
        fn = PAGES[choice]
        if fn is not None:
            fn()

    render_footer()


if __name__ == "__main__":
    main()
