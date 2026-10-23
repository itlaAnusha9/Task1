import streamlit as st
import json

from app.compare import compare_configs

st.set_page_config(
    page_title="Configuration Upgrade Tool",
    layout="wide"
)

st.title("Configuration Upgrade Validation Tool")

file_a = st.file_uploader(
    "Upload Current Configuration (File A)",
    type=["json"]
)

file_b = st.file_uploader(
    "Upload Target Configuration (File B)",
    type=["json"]
)

if file_a and file_b:

    config_a = json.load(file_a)

    config_b = json.load(file_b)

    st.success("Files Uploaded Successfully")

    if st.button("Compare Configurations"):

        result = compare_configs(
            config_a,
            config_b
        )

        st.subheader("Added Parameters")
        st.json(result["added"])

        st.subheader("Removed Parameters")
        st.json(result["removed"])

        st.subheader("Modified Parameters")
        st.json(result["modified"])

        st.subheader("Unchanged Parameters")
        st.json(result["unchanged"])