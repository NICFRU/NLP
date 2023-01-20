import streamlit as st
from utils import  html_reader


def show_explore_page():
    st.subheader("Explore the data and results")

    st.write(
        """
    ### LOOK AT MY DATA
    """
    )

    html_reader("Hatespeechvergleich-je-Partei.html")
    html_reader("Hatespeechvergleich-je-Partei-und-Themengebiet.html")


