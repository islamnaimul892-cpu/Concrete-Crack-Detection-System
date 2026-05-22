import streamlit as st
from api_calling import content_generator
from PIL import Image

st.title("Concrete Crack Detection System")
st.markdown("Upload Concrete Surface Image")
st.divider()

with st.sidebar:
    st.header("Images")
    images = st.file_uploader(
        "Uploaded Concrete Surface Images and Click the Button",
        type = ['jpg','jpeg','png'],
        accept_multiple_files = True
    )
    pil_images = []

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)
        
    if images :
        col = st.columns(len(images))
        st.subheader("Uploaded Concrete Surface Images")
        for i,img in enumerate(images):
            with col[i]:
                st.image(img)

    pressed = st.button("Analyze Crack",type = "primary")


if pressed:
    if not images:
        st.error("You must upload at least 1 image")

    if images:
        with st.container(border = True):
            st.subheader("Inspection Report")
            with st.spinner("Inspecting structure..."):
                generated_content = content_generator(pil_images)
                st.markdown(generated_content)




   