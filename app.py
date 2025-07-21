# app.py

import streamlit as st
import weaviate
import os
import base64
from weaviate.classes.generate import GenerativeConfig, GenerativeParameters
from dotenv import load_dotenv

load_dotenv(override=True)

# --- Connect to Weaviate ---
@st.cache_resource
def get_weaviate_client():
    return weaviate.connect_to_weaviate_cloud(
        cluster_url=os.getenv("WEAVIATE_URL"),
        auth_credentials=os.getenv("WEAVIATE_API_KEY"),
        headers={
            "X-Cohere-Api-Key": os.getenv("COHERE_API_KEY"),
            "X-Anthropic-Api-Key": os.getenv("ANTHROPIC_API_KEY"),
        }
    )

client = get_weaviate_client()
pages = client.collections.get("Pages")

# --- Streamlit UI ---
st.title("Multimodal RAG")

query = st.text_input("Ask a question about the document:", value="Latest developments in retrieval augmented generation")
top_k = st.number_input("Number of results", min_value=1, max_value=10, value=3)

if st.button("Search"):
    # --- Stage 1: Search ---
    with st.spinner("Searching for relevant pages..."):
        response = pages.query.near_text(
            query=query,
            limit=top_k,
            return_properties=["document_title", "page_image", "filename"],
        )

    st.subheader("Relevant Pages")
    objects = response.objects
    num_cols = 3
    rows = [objects[i:i+num_cols] for i in range(0, len(objects), num_cols)]
    for row in rows:
        cols = st.columns(num_cols)
        for col, o in zip(cols, row):
            b64_img = o.properties["page_image"]
            filename = o.properties.get("filename", "")
            doc_title = o.properties.get("document_title", "")
            # Show small preview in the column
            img_bytes = base64.b64decode(b64_img)
            with col:
                st.markdown(f"**{filename}**<br/>{doc_title}", unsafe_allow_html=True)
                st.image(img_bytes, width=120)

    # Show expanders for enlarged images below the grid
    for o in objects:
        b64_img = o.properties["page_image"]
        filename = o.properties.get("filename", "")
        doc_title = o.properties.get("document_title", "")
        img_bytes = base64.b64decode(b64_img)
        with st.expander(f"{filename} - {doc_title} (Click to enlarge)"):
            st.image(img_bytes, caption=doc_title, use_container_width=True)

    # --- Stage 2: Generation (background) ---
    with st.spinner("Generating answer..."):
        prompt = GenerativeParameters.grouped_task(
            prompt=query,
            image_properties=["page_image"],
        )
        gen_response = pages.generate.near_text(
            query=query,
            limit=top_k,
            grouped_task=prompt,
            return_properties=["document_title", "page_image", "filename"],
            generative_provider=GenerativeConfig.anthropic()
        )
    st.subheader("Answer")
    st.write(gen_response.generative.text)

