import streamlit as st

# Page config
st.set_page_config(page_title="About - NeuroVision", layout="wide")

# Inject Font Awesome for social icons
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Inject CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style_about.css")

# Hide the left‑hand Streamlit sidebar
st.markdown("""
    <style>
      [data-testid="stSidebar"] {
        display: none !important;
      }
    </style>
""", unsafe_allow_html=True)

# Navbar with "NeuroVision" on left
st.markdown(
    """
    <div class="navbar">
    <div class="logo"> 
        <span class="neuro">NEURO </span><span class="vision"> VISION</span>
    </div>
    <div class="nav-links">
        <a href="/?page=home">
            <i class="fas fa-home"></i> HOME
        </a>
        <a href="/about">
            <i class="fas fa-info-circle"></i> ABOUT
        </a>
    </div>
</div>

    """,
    unsafe_allow_html=True
)

st.markdown("<div class='centered-title'>About <span class='neuro'>NEURO</span><span class='vision'>VISION</span></div>", unsafe_allow_html=True)

st.markdown("""
    <div class="card">
        <div class="centered-text">
            NeuroVision was created to assist medical professionals and researchers in the analysis of brain MRI scans. 
            Our mission is to leverage advanced artificial intelligence to improve the accuracy, speed, and accessibility of brain tumor detection and classification.
            <br>
            We aim to support healthcare providers with additional insights that may assist in their diagnostic process, ultimately contributing to better patient outcomes through earlier and more accurate detection of brain tumors.
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="info-card card-left">
        <h2>Advanced <span class="highlight">AI Technology</span></h2>
        <p>Our platform leverages state-of-the-art deep learning models specifically trained on thousands of brain MRI scans to provide accurate detection and classification of tumors.</p>
        <ul class="custom-list">
            <li> Detection of four categories: No Tumor, Meningioma, Glioma, and Pituitary tumors 🧠</li>
            <li> Precise tumor segmentation with region highlighting ✅</li>
            <li> High accuracy rates comparable to expert radiologists 💯</li>
            <li> Fast processing times for immediate results 💡</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='section-header'>Type of <span >Tumors</span> Detected</div>",
    unsafe_allow_html=True
)


st.markdown("""
    <div class="tumor-types-container">
        <div class="tumor-card meningioma">
            <div class="tumor-card-title"><strong>Meningiomas</strong></div>
            <div class="tumor-card-desc">Meningiomas are tumors that develop in the meninges, the protective layers covering the brain and spinal cord.</div>
        </div>
        <div class="tumor-card glioma">
            <div class="tumor-card-title"><strong>Gliomas</strong></div>
            <div class="tumor-card-desc">Gliomas originate from glial cells and are known for their rapid growth and invasive nature.</div>
        </div>
        <div class="tumor-card pituitary">
            <div class="tumor-card-title"><strong>Pituitary Tumors</strong></div>
            <div class="tumor-card-desc">Pituitary tumors affect the pituitary gland and can impact hormone production, leading to various health issues.</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        <p>CONNECT WITH US:
            <a href="https://www.linkedin.com/in/jyoti-singh-b02570254/" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/jyotii-19" target="_blank"><i class="fab fa-github"></i></a>
        </p>
    </div>
""", unsafe_allow_html=True)
