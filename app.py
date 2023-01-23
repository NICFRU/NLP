import streamlit as st
from time import sleep


from select_page import select_page
from predict_page import show_predict_page
from zsm_page import show_nlp_zsmf
from explore_page import show_explore_page

st.set_page_config(
    page_title = "NLP Frontend",
    layout="wide"
    )

def draw_all(key,plot=False):
    st.write("""
    # NLP Projekt Frontend

    ## Folgende Pages können gefunden werden
    1. Visualisierung
    2. NLP Zusammenfassung
    3. NLP Modelle

    """)

with st.sidebar:
    draw_all("sidebar")

def main():
    st.title("NLP Frontend")
    st.write("---")
    menu = ["--select--", "Visualisierung","NLP Zusammenfassung",  "NLP Modelle"]
    page = st.sidebar.selectbox("Choose your page:", menu)

    if page =="--select--":
        select_page()
    
    elif page == "NLP Modelle":
        show_predict_page()

    elif page == "Visualisierung":
        show_explore_page()
    
    elif page == "NLP Zusammenfassung":
        show_nlp_zsmf()



if __name__ == "__main__":
    main()