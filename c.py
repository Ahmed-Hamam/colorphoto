import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import io
import base64

# Constants
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Function to enhance the brightness of the input image
def enhance_image(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    enhanced_image = enhancer.enhance(factor)
    return ImageOps.invert(enhanced_image)  # Invert colors after enhancement

# Function to process and display the image
def fix_image(upload=None):
    if upload:
        image = Image.open(upload)
    else:
        # Load the default image
        image = Image.open("zebra.jpg")

    # Create two columns for layout
    col1, col2 = st.columns(2)

    # Display input image in the first column
    with col1:
        st.image(image, caption="Input Image", use_column_width=True)

    # Process the image with the given enhancement factor
    enhanced_inverted_image = enhance_image(image, factor)

    # Display processed image in the second column
    with col2:
        st.image(enhanced_inverted_image, caption="Enhanced and Inverted Image", use_column_width=True)

    # Provide download option for the enhanced and inverted image
    buf = io.BytesIO()
    enhanced_inverted_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.sidebar.download_button(
        label="Download Enhanced and Inverted Image",
        data=byte_im,
        file_name="enhanced_inverted_image.png",
        mime="image/png"
    )
main_bg = "ocean-8285752_1280.jpg"
main_bg_ext = "jpg"

side_bg = "astronomy-1867616_1280.jpg"
side_bg_ext = "jpg"

# Streamlit app setup
st.title("Image Enhancer and Inverter")
st.write("Upload an image, adjust the brightness, and get its color inverted.")

# Sidebar for additional controls
st.sidebar.write("## Upload and Download :gear:")

# File uploader in the sidebar for image input
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# Add a slider to adjust the enhancement factor in the sidebar
factor = st.sidebar.slider("Enhancement Factor", min_value=0.5, max_value=3.0, value=1.0, step=0.1)

# Check the uploaded file size and use the uploaded or default image
if uploaded_file is not None:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=uploaded_file)
else:
    fix_image("zebra.jpg")
    
CURRENT_THEME = "dark"
IS_DARK_THEME = True
# Add custom CSS for background color
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://pixabay.com/get/g49cf24c05c1df5dff67b1b00a479de1ccafd0517cae82b4e50d02eafc21463303527cca3601d6bd455050a19e3182d70a185b63b8319e01fbcd46706dc84dec9_1280.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
