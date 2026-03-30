import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ── Page Config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Scripbox RM Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide Streamlit chrome for a clean dashboard look ─────────
st.markdown(
    """
    <style>
        /* Hide hamburger menu, header, footer */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Remove default padding so the dashboard fills the screen */
        .stMainBlockContainer {
            padding-top: 0 !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            padding-bottom: 0 !important;
        }

        /* Make the iframe fill the viewport */
        iframe {
            width: 100% !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Load and render the HTML dashboard ───────────────────────
# Resolve path relative to this script's location (works on Community Cloud)
SCRIPT_DIR = Path(__file__).parent.resolve()

@st.cache_data
def load_dashboard():
    html_path = SCRIPT_DIR / "MF_NAVigator.html"
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

html_content = load_dashboard()

# Render inside an iframe using components.html
components.html(html_content, height=900, scrolling=True)
