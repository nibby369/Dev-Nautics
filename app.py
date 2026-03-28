import streamlit as st

st.set_page_config(
    page_title="Dev Nautics Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Sora:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0a2e1f 0%, #0d3d28 60%, #0f4a30 100%);
    border-right: 1px solid #1a5c38;
}
section[data-testid="stSidebar"] * {
    color: #d4f0e0 !important;
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stMultiSelect label {
    color: #7ec8a0 !important;
    font-size: 12px !important;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* Main background */
.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    background: #f7faf8;
}

/* Metric cards */
div[data-testid="metric-container"] {
    background: #ffffff;
    border: 1px solid #e0ede6;
    border-radius: 12px;
    padding: 16px 20px;
    box-shadow: 0 1px 4px rgba(13,61,40,0.06);
}
div[data-testid="metric-container"] label {
    color: #5a8a70 !important;
    font-size: 12px !important;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
    color: #0d3d28 !important;
    font-family: 'Sora', sans-serif;
    font-size: 26px !important;
    font-weight: 700;
}
div[data-testid="metric-container"] div[data-testid="stMetricDelta"] {
    font-size: 12px !important;
}

/* Page headers */
h1 { font-family: 'Sora', sans-serif !important; color: #0d3d28 !important; font-weight: 700 !important; }
h2 { font-family: 'Sora', sans-serif !important; color: #0d3d28 !important; font-weight: 600 !important; }
h3 { color: #1a5c38 !important; font-weight: 600 !important; }

/* Dividers */
hr { border-color: #d4ead9 !important; }

/* Tabs */
div[data-baseweb="tab-list"] {
    background: #eaf4ee;
    border-radius: 8px;
    padding: 4px;
    gap: 4px;
}
div[data-baseweb="tab"] {
    border-radius: 6px !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}
div[data-baseweb="tab"][aria-selected="true"] {
    background: #1D9E75 !important;
    color: white !important;
}

/* Tables */
div[data-testid="stDataFrame"] {
    border: 1px solid #e0ede6;
    border-radius: 10px;
    overflow: hidden;
}

/* Expanders */
div[data-testid="stExpander"] {
    border: 1px solid #e0ede6 !important;
    border-radius: 10px !important;
    background: white;
}

/* Badges / info boxes */
.dn-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
}
.badge-green  { background: #d4f0e0; color: #0a5c30; }
.badge-amber  { background: #fef3d7; color: #8a5c00; }
.badge-red    { background: #fde8e8; color: #8a1010; }
.badge-blue   { background: #e0eeff; color: #1a3d8a; }

/* Section title style */
.section-title {
    font-family: 'Sora', sans-serif;
    font-size: 13px;
    font-weight: 600;
    color: #5a8a70;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
    margin-top: 0.5rem;
}

/* Chart containers */
.chart-card {
    background: white;
    border-radius: 12px;
    border: 1px solid #e0ede6;
    padding: 16px;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0 0.5rem;'>
        <div style='font-family:Sora,sans-serif; font-size:22px; font-weight:700;
                    color:#7dffc0; letter-spacing:-0.5px;'>Dev Nautics</div>
        <div style='font-size:11px; color:#7ec8a0; margin-top:2px;'>
            Education CRM · Surat</div>
    </div>
    <hr style='border-color:#1a5c38; margin: 0.8rem 0;'/>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title' style='color:#7ec8a0'>Navigation</div>", unsafe_allow_html=True)

    pages = {
        "🏠 Executive Overview": "Overview",
        "👦 Student Management": "Students",
        "📋 Services": "Services",
        "📦 Products & Inventory": "Products",
        "💰 Revenue & Finance": "Finance",
        "📣 Leads & Enquiries": "Leads",
        "⭐ Testimonials & Feedback": "Feedback",
        "📊 Academic Performance": "Performance",
        "👩‍🏫 Staff & Operations": "Staff",
        "📡 Social & Digital": "Social",
    }

    selected = st.radio("", list(pages.keys()), label_visibility="collapsed")

    st.markdown("<hr style='border-color:#1a5c38; margin: 1rem 0;'/>", unsafe_allow_html=True)
    st.markdown("<div class='section-title' style='color:#7ec8a0'>Global Filters</div>", unsafe_allow_html=True)

    selected_year = st.selectbox("Academic Year", ["2024-25", "2023-24"], index=0)
    selected_class = st.multiselect(
        "Class Filter",
        ["Jr.Kg", "Sr.Kg", "Class 1", "Class 2", "Class 3", "Class 4",
         "Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10"],
        default=[]
    )
    selected_service = st.multiselect(
        "Service Filter",
        ["Tuition", "Olympiad", "Handwriting", "Worksheet", "Online Math",
         "Robotics", "Skill Enhancement"],
        default=[]
    )

    st.markdown("""
    <hr style='border-color:#1a5c38; margin: 1rem 0;'/>
    <div style='font-size:10px; color:#7ec8a0; text-align:center; line-height:1.6;'>
        U-33 Corner Point, Citylight<br>Surat - 395007<br>
        📞 8866713206<br>
        <a href='https://devnautics.com' style='color:#7dffc0'>devnautics.com</a>
    </div>
    """, unsafe_allow_html=True)

# Store filters in session state
st.session_state["selected_year"] = selected_year
st.session_state["selected_class"] = selected_class
st.session_state["selected_service"] = selected_service

# ── Route to page ────────────────────────────────────────────────────────────
page_key = pages[selected]

if page_key == "Overview":
    from pages import page_overview; page_overview.render()
elif page_key == "Students":
    from pages import page_students; page_students.render()
elif page_key == "Services":
    from pages import page_services; page_services.render()
elif page_key == "Products":
    from pages import page_products; page_products.render()
elif page_key == "Finance":
    from pages import page_finance; page_finance.render()
elif page_key == "Leads":
    from pages import page_leads; page_leads.render()
elif page_key == "Feedback":
    from pages import page_feedback; page_feedback.render()
elif page_key == "Performance":
    from pages import page_performance; page_performance.render()
elif page_key == "Staff":
    from pages import page_staff; page_staff.render()
elif page_key == "Social":
    from pages import page_social; page_social.render()
