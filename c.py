import streamlit as st
from PIL import Image, ImageOps
import io

# Function to invert the colors of the input image
def predict(image):
    return ImageOps.invert(image)

# Streamlit app setup
st.title("Image Inverter")
st.write("Upload an image and get its color inverted.")

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process the image and display the result
    inverted_image = predict(image)
    st.image(inverted_image, caption="Inverted Image", use_column_width=True)

    # Provide download option for the inverted image
    buf = io.BytesIO()
    inverted_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="Download Inverted Image",
        data=byte_im,
        file_name="inverted_image.png",
        mime="image/png"
    )
