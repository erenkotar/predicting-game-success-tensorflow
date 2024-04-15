import streamlit as st
def about():
    expander = st.sidebar.expander('**About**')
    expander.write("This tool is prepared by [👨‍💻 Eren KOTAR](https://linktr.ee/erenkotar)")
    expander.write("Feel free to share your feedback :smiley:")
    expander.write("*Last update: 2023-10-13*")