from funcs import about
import streamlit as st

about()
st.sidebar.success("Go to Inference Page to make predictions :sunglasses:")

# st.image("data/GPLogo.png")

st.write("""
### Welcome to prediction model in Streamlit!
This Streamlit Web page is designed to:    
- Make experiments using pre-trained prediction models
- Test -pre-trained models
- Extract insights using your inputs and the model's outputs
""")

