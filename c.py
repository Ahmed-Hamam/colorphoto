import gradio as gr
from PIL import Image, ImageOps

def predict(image):
    # Example: invert the image colors
    return ImageOps.invert(image)

# Custom CSS to hide the download button
custom_css = """
.gr-button.gr-button--small.download-button {
    display: none;
}
"""

# Create the Gradio interface
interface = gr.Interface(
    fn=predict,  # The function to wrap
    inputs=gr.Image(type="pil"),  # Input type is an image
    outputs=gr.Image(type="pil"),  # Output type is an image
    title="Image Inverter",  # Title of the app
    description="Upload an image and get its color inverted.",  # Description
    css=custom_css  # Apply custom CSS to hide the download button
)

# Launch the app
interface.launch()