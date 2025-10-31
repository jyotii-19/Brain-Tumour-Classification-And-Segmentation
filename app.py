import streamlit as st

# Page config
st.set_page_config(page_title="Home-NeuroVision", layout="wide")

# Inject Font Awesome for social icons
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)


# Inject CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style_home.css")

# Hide Streamlit's sidebar
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar-style navigation simulation
query_params = st.query_params
page = query_params.get("page", "home")

# Navbar with "NeuroVision" on left
st.markdown(
    """
    <div class="navbar">
    <div class="logo"> 
        <span class="neuro">NEURO</span><span class="vision">VISION</span>
    </div>
    <div class="nav-links">
        <a href="/?page=home">
            <i class="fas fa-home"></i> HOME
        </a>
        <a href="/about">
            <i class="fas fa-info-circle"></i> ABOUT
        </a>
        <a href="/classifierAndSegmenter">
            <i class="fas fa-sign-in-alt"></i> START HERE
        </a>
    </div>
</div>

    """,
    unsafe_allow_html=True
)

# Page router
if page == "home":
    st.markdown("""
        <h1 style='font-size: 3.5rem;  color: white ;line-height: 1.2;'>Detect Early, Treat Better –<br> AI for Brain Tumor Diagnosis</h1>
        <p style='font-size: 1.3rem; font-style: italic; margin-top: 0.5 rem; font-weight: bold;'>
            Harnessing the Power of Deep Learning for Accurate Brain Tumor Detection,<br> Segmentation and Early Diagnosis—<br>
            Because Every Second Counts ⭐.
        </p>
        """, unsafe_allow_html=True)

    # Button with hover
    st.markdown("""
        <a href="/classifierAndSegmenter" class="try-now">
            <button>TRY NOW</button>
        </a>
    """, unsafe_allow_html=True)

    # 3 Cards
    st.markdown("""
        <div class="cards-container">
            <div class="card">
                <div class="icon">📤</div>
                <div class="card-title"><strong>Upload MRI Scan</strong></div>
                <div class="card-desc">Simply upload your MRI scan image in common formats (JPEG, PNG, or DICOM).</div>
            </div>
            <div class="card">
                <div class="icon">🧠</div>
                <div class="card-title"><strong>AI Analysis</strong></div>
                <div class="card-desc">Our deep learning model analyzes the scan to detect and classify potential tumors.</div>
            </div>
            <div class="card">
                <div class="icon">📄</div>
                <div class="card-title"><strong>View Results</strong></div>
                <div class="card-desc">See classification results with segmented images highlighting tumor regions.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>CONNECT WITH US:
            <a href="https://www.linkedin.com/in/jyoti-singh-b02570254/" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/jyotii-19" target="_blank"><i class="fab fa-github"></i></a>
        </p>
    </div>
""", unsafe_allow_html=True)

