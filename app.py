# app.py — portfolio entry point
# All content lives in config.py. All UI logic lives in components.py.
# This file only handles routing and page config.

import streamlit as st
from components import (
    load_css,
    render_header,
    render_about,
    render_contact,
    render_projects,
    render_why_hire,
    render_skills,
    render_certifications,
    render_resume,
    render_personal,
    render_footer,
)

# ── Page registry: label → render function ──────────────────
# To add a new section: add an entry here + a render_* in components.py.
PAGES: dict[str, callable | None] = {
    "All":              None,           # special: renders every section
    "About Me":         render_about,
    "Contact":          render_contact,
    "Projects":         render_projects,
    "Why Hire Me?":     render_why_hire,
    "Tech Stack":       render_skills,
    "Certifications":   render_certifications,
    "Resume":           render_resume,
    "Personal":         render_personal,
}


def set_page_config() -> None:
    st.set_page_config(
        page_title="Sarthak Shandilya | Data Science Portfolio",
        page_icon=None,
        layout="wide",
        initial_sidebar_state="auto",
    )


def render_sidebar() -> str:
    """Render the navigation sidebar and return the selected page label."""
    st.sidebar.markdown(
        '<div class="nav-header">Navigation</div>',
        unsafe_allow_html=True,
    )
    return st.sidebar.radio("", list(PAGES.keys()), label_visibility="collapsed")


def main() -> None:
    set_page_config()
    load_css()

    choice = render_sidebar()
    render_header()

    if choice == "All":
        for label, fn in PAGES.items():
            if fn is not None:
                fn()
        render_footer()
    else:
        PAGES[choice]()


if __name__ == "__main__":
    main()
