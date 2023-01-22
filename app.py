import streamlit as st
from time import sleep


from select_page import select_page
from predict_page_1 import show_predict_page_1
from explore_page import show_explore_page

st.set_page_config(
    page_title = "NLP Frontend",
    layout="wide"
    )

def draw_all(key,plot=False):
    st.write("""
    # NLP Projekt Frontend

    ## Folgende Pages können gefunden werden
    1. Visualiesierung
    2. NLP Modelle

    """)

with st.sidebar:
    draw_all("sidebar")

def main():
    st.title("NLP Frontend")
    st.write("---")
    menu = ["--select--", "Visualiesierung",  "NLP Modelle"]
    page = st.sidebar.selectbox("Choose your page:", menu)

    if page =="--select--":
        select_page()
    
    elif page == "NLP Modelle":
        show_predict_page_1()

    elif page == "Visualiesierung":
        show_explore_page()



if __name__ == "__main__":
    main()