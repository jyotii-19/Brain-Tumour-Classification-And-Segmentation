import streamlit as st

# Page config
st.set_page_config(page_title="Brain Tumor Classifier & Segmenter - NeuroVision", layout="wide")

import numpy as np
import cv2
import time
from PIL import Image
from skimage.transform import resize
from tensorflow.keras.models import load_model

# Inject Font Awesome for social icons
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Inject CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style_model.css")

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


# ------------------ Constants ------------------ #
CLASSIFICATION_LABELS = ['glioma', 'meningioma', 'notumor', 'pituitary']
CLASS_IMAGE_SIZE = 200
SEGMENTATION_IMAGE_SIZE = 512

# ------------------ Load Models ------------------ #
@st.cache_resource
def load_classification_model():
    return load_model("brain_tumor_model.h5")

@st.cache_resource
def load_segmentation_model():
    return load_model("tumor_segmentation_model.h5", compile=False)

classification_model = load_classification_model()
segmentation_model = load_segmentation_model()

# ------------------ Classification Preprocessing ------------------ #
def preprocess_for_classification(image_file):
    image = Image.open(image_file).convert('L')  # Grayscale
    image = np.array(image)

    # Apply filters and colormap
    image = cv2.bilateralFilter(image, 2, 50, 50)
    image = cv2.applyColorMap(image, cv2.COLORMAP_BONE)

    image = cv2.resize(image, (CLASS_IMAGE_SIZE, CLASS_IMAGE_SIZE))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# ------------------ Segmentation Preprocessing ------------------ #
def preprocess_for_segmentation(image_file):
    # Load and convert to grayscale
    original_image = Image.open(image_file).convert("L")  # 'L' = 1-channel grayscale
    
    # Resize to 128x128
    resized_image = original_image.resize((128, 128))
    
    # Convert to NumPy and normalize
    image_np = np.array(resized_image) / 255.0  # Scale 0-1
    
    # Expand dims: (128,128) → (128,128,1) → (1,128,128,1)
    image_np = np.expand_dims(image_np, axis=-1)  # Add channel dimension
    image_np = np.expand_dims(image_np, axis=0)   # Add batch dimension
    
    return original_image, image_np

# ------------------ Upsample Function ------------------ #
def upsample_mask(mask):
    return resize(mask, (SEGMENTATION_IMAGE_SIZE, SEGMENTATION_IMAGE_SIZE), preserve_range=True, anti_aliasing=True).astype(np.uint8)

# ------------------ Predict Segmentation ------------------ #
def predict_segmentation(image_tensor):
    pred_mask = segmentation_model.predict(image_tensor)[0, :, :, 0]
    pred_mask = (pred_mask > 0.5).astype(np.uint8)
    confidence = np.mean(pred_mask)
    return pred_mask, confidence

# ------------------ Overlay Function ------------------ #
def overlay_mask(original_pil, mask_np):
    original_np = np.array(original_pil.resize((SEGMENTATION_IMAGE_SIZE, SEGMENTATION_IMAGE_SIZE)))
    
    # Make sure original image is 3-channel
    if len(original_np.shape) == 2:
        original_np = cv2.cvtColor(original_np, cv2.COLOR_GRAY2BGR)

    # Prepare color mask
    color_mask = np.zeros_like(original_np)
    color_mask[:, :, 1] = mask_np * 255  # Green
    
    # Blend mask with original image
    overlay = cv2.addWeighted(original_np, 0.7, color_mask, 0.3, 0)
    return overlay

# ------------------ Streamlit UI ------------------ #

# Title and Description
st.markdown("""
    <h1 > Brain Tumor Analysis🧠</h1>
    <h4 >Upload an MRI scan to detect and analyze potential brain tumors.</h4>
    <br>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* FILE UPLOADER BOX */
    [data-testid="stFileUploader"] {
    background:#cad2c5; /* Translucent background */
    backdrop-filter: blur(10px); /* Frosted glass effect */
    -webkit-backdrop-filter: blur(10px);
    color: black;
    max-width: 800px;
    margin: 30px auto; /* center horizontally */
    background-color: #cad2c5;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    text-align: center;
    }
    
    [data-testid="stFileUploader"] * {
    color: black !important;
    font-weight: 500;
}

    [data-testid="stFileUploaderDropzone"] {
    background-color: #e9ecef !important;
    border-radius: 12px;
    padding: 25px;
    color: black !important;
    position: relative;
    text-align: center;
    margin-top: 10px; /* Reduced margin from top */
    transition: background-color 0.3s ease, box-shadow 0.3s ease;
    
    /* Elevation */
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1), 
                0 0 20px rgba(76, 175, 80, 0.2); /* Subtle green glow */
    
    /* Optional: glowing animation */
    animation: glowDropzone 2s infinite alternate;
}

/* Glowing animation for dropzone */
@keyframes glowDropzone {
    from {
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1), 
                    0 0 10px rgba(76, 175, 80, 0.2);
    }
    to {
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1), 
                    0 0 20px rgba(76, 175, 80, 0.5);
    }
}

 /* Make all dropzone text black */
[data-testid="stFileUploaderDropzone"] * {
    color: black !important;
    font-weight: 500;
}

/* Optional: Fine-tune font size */
[data-testid="stFileUploaderDropzone"] p,
[data-testid="stFileUploaderDropzone"] span,
[data-testid="stFileUploaderDropzone"] div {
    font-size: 1rem; /* Adjust if needed */
}
            
    /* Browse files button */
    [data-testid="stFileUploader"] button {
         background: linear-gradient(
        135deg,
        #F5C45E,
        #E78B48
    );
    /* Frosted‑glass effect */
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);

    /* Soft, elevated shadow */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);

    /* Border to define edges */
    border: 1px solid rgba(255, 255, 255, 0.4);

    /* Text styling */
    color: black;
    font-size: 1.2rem;
    font-weight: bold;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);

    /* Shape & spacing */
    padding: 0.8rem 2rem;
    border-radius: 12px;
    cursor: pointer;

    /* Smooth transitions */
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    [data-testid="stFileUploader"] button:hover {
        background-color: #45a049;
        color: white;
    }

    </style>
""", unsafe_allow_html=True)



uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])


# If file uploaded
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    # Create three columns and put the image in the middle one
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, use_container_width=False, width=680)

    # Caption styling + center
    st.markdown("""
        <div style="text-align: center;">
            <h3 style="color: #dee2e6; font-size: 20px;">
                UPLOADED MRI 📷
            </h3>
        </div>
    """, unsafe_allow_html=True)

    # ---- Classification ---- #
    with st.spinner("Classifying tumor type..."):
        progress_text = "🔄 Processing image and running classification model..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(0, 100, 5):
            time.sleep(0.03)
            my_bar.progress(percent_complete + 1, text=progress_text)

        class_input = preprocess_for_classification(uploaded_file)
        prediction = classification_model.predict(class_input)
        predicted_class_index = np.argmax(prediction, axis=1)[0]
        predicted_label = CLASSIFICATION_LABELS[predicted_class_index]
        confidence = np.max(prediction)

        my_bar.empty()

    st.markdown(f"<div style='text-align:center;padding:10px;max-width:400px;margin:0 auto;'><div style='background-color:#28a745;color:white;border-radius:8px;padding:10px;'><span style='font-size:18px;'><strong>Predicted Tumor Type: {predicted_label.capitalize()} 🧠</strong></span></div></div>", unsafe_allow_html=True)

    if predicted_label != 'notumor':
        with st.spinner("Segmenting tumor..."):
            original_pil, seg_input = preprocess_for_segmentation(uploaded_file)
            mask, seg_confidence = predict_segmentation(seg_input)
            upsampled_mask = upsample_mask(mask)
            segmented_overlay = overlay_mask(original_pil, upsampled_mask)

        st.markdown("""
            <div style="text-align: center;">
                <h2 style="color: white; font-size: 24px;">
                    🧬 Segmented Tumor Region
                </h2>
            </div>
        """, unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(segmented_overlay, use_container_width=False, width=680)

        st.markdown("""
            <div style="text-align: center;">
                <h3 style="color: #dee2e6; font-size: 20px;">
                    SEGMENTED MRI 🔍
                </h3>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("<div style='text-align:center;padding:10px;max-width:400px;margin:0 auto;'><div style='background-color:#e63946;color:white;border-radius:8px;padding:10px;'><span style='font-size:18px;'>Segmentation not required 🤗 </span></div></div>", unsafe_allow_html=True)

    



st.markdown("""
    <div class="footer">
        <p>CONNECT WITH US:
            <a href="https://www.linkedin.com/in/jyoti-singh-b02570254/" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/jyotii-19" target="_blank"><i class="fab fa-github"></i></a>
        </p>
    </div>
""", unsafe_allow_html=True)
