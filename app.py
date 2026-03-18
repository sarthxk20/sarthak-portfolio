# app.py — Portfolio entry point.
# All content lives in config.py. All UI logic lives in components.py.
# This file only handles page config and routing.

from __future__ import annotations

from collections.abc import Callable

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

# ── Page Registry ──────────────────────────────────────────────────────────────
# To add a section: add an entry here + a render_* function in components.py.
PAGES: dict[str, Callable[[], None] | None] = {
    "All":            None,           # Special: renders every section in order
    "About Me":       render_about,
    "Projects":       render_projects,
    "Tech Stack":     render_skills,
    "Certifications": render_certifications,
    "Why Hire Me?":   render_why_hire,
    "Resume":         render_resume,
    "Contact":        render_contact,
    "Personal":       render_personal,
}


def set_page_config() -> None:
    st.set_page_config(
        page_title="Sarthak Shandilya | Data Scientist",
        page_icon="🔬",
        layout="wide",
        initial_sidebar_state="auto",
    )


def render_sidebar() -> str:
    """Render navigation sidebar and return the selected page label."""
    st.sidebar.markdown(
        '<div class="nav-header">// NAVIGATE</div>',
        unsafe_allow_html=True,
    )
    return st.sidebar.radio(
        label="Navigation",
        options=list(PAGES.keys()),
        label_visibility="collapsed",
    )


def main() -> None:
    set_page_config()
    load_css()

    choice = render_sidebar()
    render_header()

    if choice == "All":
        for fn in PAGES.values():
            if fn is not None:
                fn()
        render_footer()
    else:
        render_fn = PAGES[choice]
        if render_fn is not None:
            render_fn()


if __name__ == "__main__":
    main()
