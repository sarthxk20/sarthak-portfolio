# components.py — All UI rendering logic.
# Content lives in config.py. Routing lives in app.py.

from __future__ import annotations

import streamlit as st
from config import (
    PERSONAL,
    STATS,
    PROJECTS,
    SKILLS,
    CERTIFICATIONS,
    WHY_HIRE,
    PERSONAL_SECTION,
)

# ── CSS ────────────────────────────────────────────────────────────────────────

def load_css() -> None:
    """Inject global styles into the Streamlit app."""
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600;700&display=swap');

        /* ── Root & Reset ── */
        :root {
            --bg:        #0B0F1A;
            --surface:   #111827;
            --border:    #1E2A3A;
            --accent:    #00E5FF;
            --gold:      #FFD166;
            --text:      #E2E8F0;
            --muted:     #64748B;
            --mono:      'Space Mono', monospace;
            --sans:      'DM Sans', sans-serif;
            --radius:    12px;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: var(--bg) !important;
            color: var(--text) !important;
            font-family: var(--sans) !important;
        }

        /* Hide Streamlit chrome */
        #MainMenu, footer, header { visibility: hidden; }
        [data-testid="stToolbar"] { display: none; }
        .block-container { padding: 2rem 3rem !important; max-width: 1100px; }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background: var(--surface) !important;
            border-right: 1px solid var(--border) !important;
        }
        [data-testid="stSidebar"] * { color: var(--text) !important; }
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

        /* ── Shared Utilities ── */
        .section-label {
            font-family: var(--mono);
            font-size: 0.65rem;
            letter-spacing: 0.2em;
            color: var(--accent);
            text-transform: uppercase;
            margin-bottom: 0.4rem;
        }
        .section-title {
            font-family: var(--sans);
            font-size: 1.9rem;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }
        .divider {
            border: none;
            border-top: 1px solid var(--border);
            margin: 2.5rem 0;
        }
        a { color: var(--accent); text-decoration: none; }
        a:hover { text-decoration: underline; }

        /* ── Hero ── */
        .hero-wrap {
            padding: 3.5rem 0 2rem;
            position: relative;
        }
        .hero-mono {
            font-family: var(--mono);
            font-size: 0.75rem;
            color: var(--accent);
            letter-spacing: 0.12em;
            margin-bottom: 1rem;
        }
        .hero-name {
            font-size: 3.5rem;
            font-weight: 700;
            line-height: 1.05;
            color: var(--text);
            margin-bottom: 0.5rem;
        }
        .hero-name span { color: var(--accent); }
        .hero-title {
            font-family: var(--mono);
            font-size: 1rem;
            color: var(--muted);
            margin-bottom: 1.2rem;
        }
        .hero-tagline {
            font-size: 1.3rem;
            font-weight: 300;
            color: var(--text);
            max-width: 540px;
            line-height: 1.6;
            margin-bottom: 2rem;
            border-left: 3px solid var(--accent);
            padding-left: 1rem;
        }
        .hero-badges { display: flex; gap: 0.75rem; flex-wrap: wrap; }
        .badge {
            font-family: var(--mono);
            font-size: 0.7rem;
            padding: 0.35rem 0.85rem;
            border-radius: 999px;
            letter-spacing: 0.05em;
        }
        .badge-outline {
            border: 1px solid var(--accent);
            color: var(--accent);
        }
        .badge-fill {
            background: var(--accent);
            color: var(--bg);
            font-weight: 700;
        }
        .hero-cta { display: flex; gap: 1rem; margin-top: 1.8rem; flex-wrap: wrap; }
        .cta-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.65rem 1.4rem;
            border-radius: var(--radius);
            font-family: var(--mono);
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            cursor: pointer;
            transition: all 0.2s ease;
            text-decoration: none !important;
        }
        .cta-primary {
            background: var(--accent);
            color: var(--bg) !important;
            border: 2px solid var(--accent);
        }
        .cta-primary:hover { background: transparent; color: var(--accent) !important; }
        .cta-secondary {
            background: transparent;
            color: var(--text) !important;
            border: 2px solid var(--border);
        }
        .cta-secondary:hover { border-color: var(--accent); color: var(--accent) !important; }

        /* ── Stats Strip ── */
        .stats-wrap {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1px;
            background: var(--border);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            overflow: hidden;
            margin: 2rem 0;
        }
        .stat-cell {
            background: var(--surface);
            padding: 1.2rem 1.5rem;
            text-align: center;
        }
        .stat-value {
            font-family: var(--mono);
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--accent);
            line-height: 1;
        }
        .stat-label {
            font-size: 0.75rem;
            color: var(--muted);
            margin-top: 0.3rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }

        /* ── Project Cards ── */
        .project-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 2rem;
            margin-bottom: 1.5rem;
            transition: border-color 0.2s ease;
            position: relative;
            overflow: hidden;
        }
        .project-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: linear-gradient(90deg, var(--accent-color, #00E5FF), transparent);
        }
        .project-card:hover { border-color: var(--accent); }
        .project-header { display: flex; align-items: flex-start; gap: 1rem; margin-bottom: 1.2rem; }
        .project-emoji { font-size: 2rem; line-height: 1; }
        .project-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 0.2rem;
        }
        .project-tag {
            font-family: var(--mono);
            font-size: 0.65rem;
            color: var(--muted);
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }
        .psa-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
            margin: 1.2rem 0;
        }
        .psa-block {
            background: rgba(0,229,255,0.04);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 0.9rem 1rem;
        }
        .psa-label {
            font-family: var(--mono);
            font-size: 0.6rem;
            color: var(--accent);
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 0.4rem;
        }
        .psa-text { font-size: 0.85rem; color: var(--text); line-height: 1.5; }
        .project-highlights { margin: 1rem 0; padding: 0; list-style: none; }
        .project-highlights li {
            font-size: 0.82rem;
            color: var(--muted);
            padding: 0.2rem 0;
            padding-left: 1.2rem;
            position: relative;
        }
        .project-highlights li::before {
            content: '▸';
            position: absolute;
            left: 0;
            color: var(--accent);
        }
        .project-links { display: flex; gap: 0.75rem; margin-top: 1.2rem; flex-wrap: wrap; }
        .project-link {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-family: var(--mono);
            font-size: 0.7rem;
            padding: 0.4rem 0.9rem;
            border-radius: 6px;
            border: 1px solid var(--border);
            color: var(--text) !important;
            transition: all 0.15s ease;
        }
        .project-link:hover {
            border-color: var(--accent);
            color: var(--accent) !important;
            text-decoration: none !important;
        }

        /* ── Skills ── */
        .skills-group { margin-bottom: 2rem; }
        .skills-group-title {
            font-family: var(--mono);
            font-size: 0.7rem;
            color: var(--gold);
            text-transform: uppercase;
            letter-spacing: 0.15em;
            margin-bottom: 0.8rem;
        }
        .skill-row {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 0.65rem;
        }
        .skill-name {
            font-size: 0.85rem;
            color: var(--text);
            width: 140px;
            flex-shrink: 0;
        }
        .skill-bar-bg {
            flex: 1;
            height: 6px;
            background: var(--border);
            border-radius: 999px;
            overflow: hidden;
        }
        .skill-bar-fill {
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg, var(--accent), var(--gold));
        }
        .skill-pct {
            font-family: var(--mono);
            font-size: 0.65rem;
            color: var(--muted);
            width: 32px;
            text-align: right;
            flex-shrink: 0;
        }

        /* ── Certifications ── */
        .cert-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.5rem;
            display: flex;
            gap: 1.2rem;
            align-items: flex-start;
        }
        .cert-emoji { font-size: 2rem; }
        .cert-title { font-size: 1rem; font-weight: 600; color: var(--text); margin-bottom: 0.2rem; }
        .cert-meta { font-family: var(--mono); font-size: 0.65rem; color: var(--muted); margin-bottom: 0.5rem; }
        .cert-desc { font-size: 0.83rem; color: var(--muted); line-height: 1.5; margin-bottom: 0.7rem; }
        .cert-link {
            font-family: var(--mono);
            font-size: 0.68rem;
            color: var(--accent) !important;
            border: 1px solid var(--accent);
            padding: 0.3rem 0.75rem;
            border-radius: 6px;
            display: inline-block;
        }

        /* ── Why Hire ── */
        .why-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1rem;
        }
        .why-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.4rem;
            transition: border-color 0.2s;
        }
        .why-card:hover { border-color: var(--accent); }
        .why-icon {
            font-family: var(--mono);
            font-size: 0.65rem;
            color: var(--accent);
            letter-spacing: 0.1em;
            margin-bottom: 0.6rem;
        }
        .why-heading { font-weight: 600; font-size: 0.95rem; color: var(--text); margin-bottom: 0.4rem; }
        .why-body { font-size: 0.82rem; color: var(--muted); line-height: 1.6; }

        /* ── Contact ── */
        .contact-grid {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            max-width: 480px;
        }
        .contact-row {
            display: flex;
            align-items: center;
            gap: 1rem;
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 0.9rem 1.2rem;
            transition: border-color 0.2s;
            text-decoration: none !important;
        }
        .contact-row:hover { border-color: var(--accent); }
        .contact-icon { font-size: 1.2rem; }
        .contact-label { font-family: var(--mono); font-size: 0.65rem; color: var(--muted); }
        .contact-value { font-size: 0.9rem; color: var(--text); }

        /* ── Personal ── */
        .interests-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.75rem;
            margin-top: 1.5rem;
        }
        .interest-chip {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 0.9rem 1rem;
            text-align: center;
            font-size: 0.85rem;
            color: var(--text);
            transition: border-color 0.2s;
            font-family: var(--mono);
            letter-spacing: 0.04em;
        }
        .interest-chip:hover { border-color: var(--gold); }

        /* ── Footer ── */
        .footer {
            text-align: center;
            padding: 2rem 0 1rem;
            font-family: var(--mono);
            font-size: 0.65rem;
            color: var(--muted);
            border-top: 1px solid var(--border);
            margin-top: 3rem;
            letter-spacing: 0.08em;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ── Header / Hero ─────────────────────────────────────────────────────────────

def render_header() -> None:
    p = PERSONAL
    resume_btn = (
        f'<a class="cta-btn cta-primary" href="{p["resume_url"]}" target="_blank">Download Resume</a>'
        if p.get("resume_url")
        else ""
    )
    st.markdown(
        f"""
        <div class="hero-wrap">
            <div class="hero-mono">// PORTFOLIO · DATA SCIENCE</div>
            <div class="hero-name">{p["name"].split()[0]} <span>{p["name"].split()[1]}</span></div>
            <div class="hero-title">_{p["title"]}</div>
            <div class="hero-tagline">{p["tagline"]}</div>
            <div class="hero-badges">
                <span class="badge badge-fill">IBM Certified</span>
                <span class="badge badge-outline">{p["location"]}</span>
                <span class="badge badge-outline">Open to Work</span>
            </div>
            <div class="hero-cta">
                <a class="cta-btn cta-primary" href="mailto:{p['email']}">Contact Me</a>
                <a class="cta-btn cta-secondary" href="{p['github']}" target="_blank">GitHub</a>
                <a class="cta-btn cta-secondary" href="{p['linkedin']}" target="_blank">LinkedIn</a>
                {resume_btn}
            </div>
        </div>
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


# ── About ─────────────────────────────────────────────────────────────────────

def render_about() -> None:
    stats_html = "".join(
        f'<div class="stat-cell">'
        f'<div class="stat-value">{s["value"]}</div>'
        f'<div class="stat-label">{s["label"]}</div>'
        f'</div>'
        for s in STATS
    )
    st.markdown(
        f"""
        <div class="section-label">// 01 · ABOUT</div>
        <div class="section-title">Who I Am</div>
        <p style="font-size:1rem; line-height:1.75; color:var(--text); max-width:680px; margin-bottom:1.5rem;">
            {PERSONAL["bio"]}
        </p>
        <p style="font-size:0.85rem; color:var(--muted); font-family:var(--mono); margin-bottom:1.5rem;">
            Currently learning: {PERSONAL["currently_learning"]}<br/>
            Seeking: {PERSONAL["open_to"]}
        </p>
        <div class="stats-wrap">{stats_html}</div>
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


# ── Projects ──────────────────────────────────────────────────────────────────

def render_projects() -> None:
    cards_html = ""
    for p in PROJECTS:
        highlights = "".join(f"<li>{h}</li>" for h in p["highlights"])
        cards_html += f"""
        <div class="project-card" style="--accent-color:{p['badge_color']}">
            <div class="project-header">
                <div>
                    <div class="project-title">{p["title"]}</div>
                    <div class="project-tag">{p["tag"]}</div>
                </div>
            </div>
            <div class="psa-grid">
                <div class="psa-block">
                    <div class="psa-label">Problem</div>
                    <div class="psa-text">{p["problem"]}</div>
                </div>
                <div class="psa-block">
                    <div class="psa-label">Approach</div>
                    <div class="psa-text">{p["approach"]}</div>
                </div>
                <div class="psa-block">
                    <div class="psa-label">Result</div>
                    <div class="psa-text">{p["result"]}</div>
                </div>
            </div>
            <ul class="project-highlights">{highlights}</ul>
            <div class="project-links">
                <a class="project-link" href="{p['live_url']}" target="_blank">Live App</a>
                <a class="project-link" href="{p['github_url']}" target="_blank">GitHub</a>
            </div>
        </div>
        """

    st.markdown(
        f"""
        <div class="section-label">// 02 · WORK</div>
        <div class="section-title">Projects</div>
        {cards_html}
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


# ── Skills ────────────────────────────────────────────────────────────────────

def render_skills() -> None:
    groups_html = ""
    for group, items in SKILLS.items():
        rows = "".join(
            f"""
            <div class="skill-row">
                <div class="skill-name">{s["name"]}</div>
                <div class="skill-bar-bg">
                    <div class="skill-bar-fill" style="width:{s['level']}%"></div>
                </div>
                <div class="skill-pct">{s["level"]}%</div>
            </div>
            """
            for s in items
        )
        groups_html += f"""
        <div class="skills-group">
            <div class="skills-group-title">{group}</div>
            {rows}
        </div>
        """

    st.markdown(
        f"""
        <div class="section-label">// 03 · STACK</div>
        <div class="section-title">Tech Stack</div>
        {groups_html}
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


# ── Certifications ────────────────────────────────────────────────────────────

def render_certifications() -> None:
    cards_html = ""
    for c in CERTIFICATIONS:
        cards_html += f"""
        <div class="cert-card">
            <div>
                <div class="cert-title">{c["title"]}</div>
                <div class="cert-meta">{c["issuer"]} · {c["year"]}</div>
                <div class="cert-desc">{c["description"]}</div>
            </div>
        </div>
        """

    st.markdown(
        f"""
        <div class="section-label">// 04 · CREDENTIALS</div>
        <div class="section-title">Certifications</div>
        {cards_html}
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


# ── Why Hire Me ───────────────────────────────────────────────────────────────

def render_why_hire() -> None:
    cards_html = "".join(
        f"""
        <div class="why-card">
            <div class="why-icon">{w["icon"]}</div>
            <div class="why-heading">{w["heading"]}</div>
            <div class="why-body">{w["body"]}</div>
        </div>
        """
        for w in WHY_HIRE
    )

    st.markdown(
        f"""
        <div class="section-label">// 05 · VALUE</div>
        <div class="section-title">Why Hire Me?</div>
        <div class="why-grid">{cards_html}</div>
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


# ── Resume ────────────────────────────────────────────────────────────────────

def render_resume() -> None:
    resume_btn = (
        f'<a class="cta-btn cta-primary" href="{PERSONAL["resume_url"]}" target="_blank">Download Resume (PDF)</a>'
        if PERSONAL.get("resume_url")
        else '<p style="color:var(--muted);font-family:var(--mono);font-size:0.8rem;">Resume link coming soon — add your URL to config.py → PERSONAL[\'resume_url\']</p>'
    )

    st.markdown(
        f"""
        <div class="section-label">// 06 · RESUME</div>
        <div class="section-title">Resume</div>
        <p style="color:var(--muted);font-size:0.9rem;margin-bottom:1.5rem;">
            A full summary of my education, projects, skills, and certifications.
        </p>
        {resume_btn}
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


# ── Contact ───────────────────────────────────────────────────────────────────

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
                <div>
                    <div class="contact-label">EMAIL</div>
                    <div class="contact-value">{p['email']}</div>
                </div>
            </a>
            <a class="contact-row" href="{p['linkedin']}" target="_blank">
                <div>
                    <div class="contact-label">LINKEDIN</div>
                    <div class="contact-value">linkedin.com/in/sarthxk20</div>
                </div>
            </a>
            <a class="contact-row" href="{p['github']}" target="_blank">
                <div>
                    <div class="contact-label">GITHUB</div>
                    <div class="contact-value">github.com/sarthxk20</div>
                </div>
            </a>
        </div>
        <hr class="divider" />
        """,
        unsafe_allow_html=True,
    )


# ── Personal ──────────────────────────────────────────────────────────────────

def render_personal() -> None:
    ps = PERSONAL_SECTION
    chips = "".join(
        f'<div class="interest-chip">{i["label"]}</div>'
        for i in ps["interests"]
    )
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


# ── Footer ────────────────────────────────────────────────────────────────────

def render_footer() -> None:
    st.markdown(
        f'<div class="footer">© 2026 {PERSONAL["name"]} · Built with Streamlit · '
        f'<a href="{PERSONAL["github"]}" target="_blank">View Source</a></div>',
        unsafe_allow_html=True,
    )
