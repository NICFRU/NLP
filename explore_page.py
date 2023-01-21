import streamlit as st
from utils import  html_reader


def show_explore_page():
    st.subheader("Explore the data and results")

    st.write(
        """
    ### This is the Exploration Part feel free to test everything
    """
    )


    col1, col2= st.columns(2)

    with col1:
        html_reader("data/Hatespeechvergleich-je-Partei.html")

    with col2:
        html_reader("data/Hatespeechvergleich-je-Partei-und-Themengebiet.html")

    st.write("---")
    menu = ["--select--","AFD","CDU-CSU","GRUENE","LINKE","FDP","SPD"]
    PTR = st.selectbox("Auswahl der Partei:", menu)