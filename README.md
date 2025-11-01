<h1 align="center">Brain Tumor Classification and Segmentation using Deep Learning 🤖🧬💡</h1>

<p align="center">
An advanced deep learning–powered medical imaging project that performs both <b>brain tumor detection (classification)</b> and <b>region-based segmentation</b> from MRI scans.<br>
Built with a combination of <b>CNN-based classification</b> and <b>U-Net segmentation</b> models, this pipeline provides a complete solution—from tumor identification to detailed visualization—through a seamless <b>Streamlit web app</b>.
</p>

<hr>

<h2>📑 Contents</h2>

<ul>
  <li><a href="#-overview">Overview</a></li>
  <li><a href="#-features">Features</a></li>
  <li><a href="#-dataset">Dataset</a></li>
  <li><a href="#-model-architecture">Model Architecture</a></li>
  <li><a href="#-training">Training</a></li>
  <li><a href="#-inference">Inference</a></li>
  <li><a href="#-web-application">Web Application</a></li>
  <li><a href="#-results">Results</a></li>
</ul>

<hr>

<h2>🪄 Overview</h2>
<p>
This project integrates <b>classification</b> and <b>segmentation</b> models to deliver a full-scale brain tumor analysis pipeline.
The <b>classification model</b> first determines whether a tumor is present and identifies its type, while the <b>segmentation model</b> pinpoints the exact tumor regions within MRI slices.
</p>

<p>The system performs two primary tasks:</p>
<ul>
  <li><b>1. Classification:</b> Categorizes MRI scans into classes such as <i>Glioma</i>, <i>Meningioma</i>, <i>Pituitary Tumor</i>, or <i>No Tumor</i>.</li>
  <li><b>2. Segmentation:</b> Generates a pixel-wise mask highlighting the tumor area for visual understanding and clinical support.</li>
</ul>

<hr>

<h2 id="features">✨ Features</h2>

<ul>
  <li><b>Dual-Stage Pipeline:</b> Integrates classification and segmentation in one unified system.</li>
  <li><b>Efficient CNN Classifier:</b> Detects and identifies tumor types using transfer learning.</li>
  <li><b>U-Net Segmentation Model:</b> Performs precise tumor boundary segmentation from MRI slices.</li>
  <li><b>End-to-End Workflow:</b> From preprocessing to inference, everything is automated.</li>
  <li><b>Hybrid Loss Functions:</b> Combines Dice and Cross-Entropy for stable segmentation training.</li>
  <li><b>Streamlit Web App:</b> Clean, intuitive interface for uploading scans and viewing predictions in real-time.</li>
  <li><b>Performance Metrics:</b> Accuracy, Dice score, IoU, and confusion matrix visualization.</li>
  <li><b>Early Stopping:</b> Prevents overfitting by monitoring validation metrics.</li>
</ul>

<hr>

<h2>📊 Dataset</h2>

<p>
The project uses two complementary datasets for model training and evaluation:
</p>

<ul>
  <li><b>Classification Dataset:</b> <i>Brain MRI Images Dataset</i> (Kaggle) — includes MRI scans of four categories (Glioma, Meningioma, Pituitary, and No Tumor).</li>
  <li><b>Segmentation Dataset:</b> <i>Brain Tumor Dataset (Cheng et al.)</i> — structured dataset that contains T1-weighted contrast-enhanced MRI slices with tumor masks.</li>
</ul>

<h3>🧩 Preprocessing Steps</h3>
<ul>
  <li><b>Image Normalization:</b> Scales pixel intensities to [0,1].</li>
  <li><b>Resizing:</b> Standardized dimensions (128×128 for classification, 240×240 for segmentation).</li>
  <li><b>Data Augmentation:</b> Rotation, flipping, zoom, and contrast adjustments to enhance generalization.</li>
  <li><b>Label Encoding:</b> Converts class names into categorical labels for supervised learning.</li>
</ul>

<hr>

<h2 id="architecture">🏗️ Model Architecture</h2>

<p>
The system is composed of two interconnected deep learning models:
</p>

<h3>🧩 1. Classification Model (CNN)</h3>
<ul>
  <li>Built using <b>transfer learning</b> </li>
  <li>Fully connected dense layers with <b>softmax</b> output for class probabilities</li>
  <li><b>Dropout</b> regularization and <b>BatchNorm</b> for stable training</li>
  <li><b>Output:</b> Tumor type classification</li>
</ul>

<h3>🔬 2. Segmentation Model (U-Net)</h3>
<ul>
  <li>Encoder-decoder structure for spatial context preservation</li>
  <li>Skip connections between downsampling and upsampling paths</li>
  <li>Trained with <b>Dice + BCE loss</b> for accurate mask generation</li>
  <li><b>Output:</b> Binary mask highlighting tumor area</li>
</ul>

<hr>

<h2 id="training">🚧 Training</h2>

<p>
Both models were trained separately and then integrated for pipeline inference.
Training emphasizes stability, generalization, and interpretability.
</p>

<h3>⚙️ Key Training Features</h3>

<ul>
  <li><b>Transfer Learning:</b> Uses pretrained CNNs for efficient convergence in classification.</li>
  <li><b>Hybrid Loss Function:</b> Combines <b>Dice</b> and <b>Binary Cross-Entropy</b> for segmentation.</li>
  <li><b>Data Augmentation:</b> Improves robustness to MRI variability.</li>
  <li><b>Checkpointing:</b> Automatically saves best-performing weights.</li>
  <li><b>Early Stopping:</b> Monitors validation loss to avoid overfitting.</li>
  <li><b>Batch Normalization:</b> Ensures smoother gradient flow and faster convergence.</li>
</ul>

<pre style="background-color:#0d1117;color:#e6edf3;padding:16px;border-radius:10px;overflow-x:auto;font-family:'Fira Code', monospace;font-size:14px;line-height:1.6;">
# Example training setup

# Classification
python train_classification.py --epochs 25 --lr 1e-4 --batch_size 16

# Segmentation
python train_segmentation.py --epochs 20 --lr 1e-4 --batch_size 4
</pre>

<hr>

<h2 id="inference">🚀 Inference</h2>

<p>
During inference, the system first classifies the MRI scan and, if a tumor is detected, performs segmentation to highlight its boundaries.
The final result combines diagnosis (tumor type) and visualization (segmented mask).
</p>

<h3>🔍 Inference Workflow</h3>

<ul>
  <li><b>Step 1:</b> Upload an MRI scan (supports .jpg, .png, or .nii formats).</li>
  <li><b>Step 2:</b> The classification model predicts tumor presence and type.</li>
  <li><b>Step 3:</b> If tumor detected → segmentation model generates region mask.</li>
  <li><b>Step 4:</b> The app displays classification result and segmented image side-by-side.</li>
</ul>

<hr>

<h2>🌐 Web Application</h2>
<p>
  <strong>🚀 Try It Yourself</strong><br>
  Experience the complete brain tumor segmentation workflow here:<br>
  👉 <a href="https://brain-tumour-classification-and-segmentation-hyyh.streamlit.app/?page=home" target="_blank" rel="noopener noreferrer">Launch Web App</a>
</p>
<p>
A <b>Streamlit-based web app</b> serves as the front-end for both models. Users can upload MRI scans, trigger classification, view tumor masks, and interpret predictions interactively—all without writing a single line of code.
</p>

<h3>💡 Application Workflow</h3>
<ul>
  <li><b>1. Upload Section:</b> Upload MRI scans.</li>
  <li><b>3. Inference:</b> The model starts the prediction <b></li>
  <li><b>4. Output Display:</b> Tumor type and segmentation mask are displayed.</li>
</ul>

<h3>⚡ Web Application Features</h3>
<ul>
  <li>🧠 <b>Integrated Analysis:</b> Classification and segmentation in one unified interface.</li>
  <li>📈 <b>Real-time Feedback:</b> Displays overlay masks.</li>
  <li>🎨 <b>User Experience:</b> Clean and user friendly design</li>
</ul>

<hr>

<h2>📈 Results</h2>

<h3>🧮 Model Performance</h3>
<table>
<tr><th>Task</th><th>Metric</th><th>Score</th></tr>
<tr><td>Classification</td><td>Accuracy</td><td>~95%</td></tr>
<tr><td>Segmentation</td><td>Mean Dice Score</td><td>~0.70</td></tr>
<tr><td>Segmentation</td><td>IoU</td><td>~0.65</td></tr>
</table>

<h3>🧪 Training Insights</h3>
<ul>
  <li><b>Epochs:</b> Classification converged in ~20 epochs, segmentation in ~15.</li>
  <li><b>Hardware:</b> Trained on 8 GB GPU (NVIDIA RTX / Colab).</li>
  <li><b>Runtime:</b> ~2 minutes per MRI scan for full pipeline inference.</li>
</ul>

<hr>

<h2>🏥 Applications</h2>
<ul>
  <li><b>Tumor Detection:</b> Quick screening of MRI scans for possible abnormalities.</li>
  <li><b>Boundary Visualization:</b> Assists radiologists in locating tumor regions.</li>
  <li><b>Pre-Surgical Planning:</b> Provides accurate masks for medical planning.</li>
  <li><b>Educational Use:</b> Helpful for learning medical image analysis and AI integration.</li>
</ul>

<hr>

<h2>📚 References</h2>
<ul>
  <li>Cheng, J. (2017). <strong>Brain Tumor Dataset</strong>. Figshare. Dataset. <a href="https://doi.org/10.6084/m9.figshare.1512427.v5">https://doi.org/10.6084/m9.figshare.1512427.v5</a></li>

  <li>Nickparvar, M. (2021). <strong>Brain Tumor MRI Dataset</strong> [Data set].</li>

  <li>Kaggle (2021). <strong>Brain Tumor MRI Dataset</strong>. <a href="https://doi.org/10.34740/kaggle/dsv/2645886">https://doi.org/10.34740/kaggle/dsv/2645886</a></li>

  <li>Ronneberger, O., Fischer, P., & Brox, T. (2015). <strong>U-Net: Convolutional Networks for Biomedical Image Segmentation</strong>. In <em>Medical Image Computing and Computer-Assisted Intervention – MICCAI 2015</em> (pp. 234–241). Springer.</li>

  <li>Zhou, Z., et al. (2018). <strong>UNet++: A Nested U-Net Architecture for Medical Image Segmentation</strong>. In <em>Deep Learning in Medical Image Analysis and Multimodal Learning for Clinical Decision Support</em>. Springer.</li>

  <li>Koonce, B. (2021). <strong>ResNet 50</strong>. In <em>Convolutional Neural Networks with Swift for TensorFlow: Image Recognition and Dataset Categorization</em> (pp. 63–72). Apress.</li>

  <li>Sharma, A. K., Nandal, A., Dhaka, A., Zhou, L., Alhudhaif, A., Alenezi, F., & Polat, K. (2023). <strong>Brain Tumor Classification Using the Modified ResNet50 Model Based on Transfer Learning</strong>. <em>Biomedical Signal Processing and Control, 86</em>, 105299.</li>
</ul>


<hr>

<h2>🙏 Acknowledgments</h2>
<ul>
  <li><b>Figshare</b> and <b>Kaggle</b> for providing open-access Brain Tumor MRI datasets.</li>
  <li><b>TensorFlow</b> and <b>Keras</b> teams for their powerful deep learning frameworks.</li>
  <li>All researchers and open-source contributors advancing medical AI research.</li>
</ul>

<hr>

<h2>⚠️ Disclaimer</h2>
<p>
This project is intended for <b>research and educational purposes only</b>.  
It is not validated for clinical or diagnostic use.  
Consult certified medical professionals for real-world medical interpretation.
</p>

<hr>
