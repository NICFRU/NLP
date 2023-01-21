import streamlit as st
from time import sleep


from select_page import select_page
from predict_page_1 import show_predict_page_1
from explore_page import show_explore_page

st.set_page_config(
    page_title = "NLP Web App",
    layout="wide"
    )

def draw_all(key,plot=False):
    st.write("""
    # NLP Web App

    Das ist eine wundervolle Web-App die NLP Model implementiert hat.

    ## Folgende Pages können gefunden werden
    1. Exploration
    2. Topic prediction 

    """)

with st.sidebar:
    draw_all("sidebar")

def main():
    st.title("NLP Web App")
    st.write("---")
    menu = ["--select--", "Exploration",  "Topic prediction"]
    page = st.sidebar.selectbox("Choose your page:", menu)

    if page =="--select--":
        select_page()
    
    elif page == "Topic prediction":
        show_predict_page_1()

    elif page == "Exploration":
        show_explore_page()



if __name__ == "__main__":
    main()