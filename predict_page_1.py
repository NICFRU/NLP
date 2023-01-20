import streamlit as st
import pandas as pd
from classification import zeroshotNLP, hatespeachNLP, sentimentNLP
from streamlit_toggle import st_toggle_switch
import time
import streamlit as st


def show_predict_page_1():

    st.subheader(
    """
    MULTI NLP TOOL
    """
    )

    multiline = st_toggle_switch(
                                label="Multi Line Text?",
                                    key="multiswitch",
                                    default_value=False,
                                    label_after=False,
                                    inactive_color="#D3D3D3",  # optional
                                    active_color="#11567f",  # optional
                                    track_color="#29B5E8",  # optional
                                )

    st.write(
    """
    Gib hier deinen Text ein:
    """
    )

    txt = st.text_area("Your text:")


    zeroshotbox = st.checkbox('Zero Shot Calssification')
    hatespeachbox = st.checkbox('Hate Speach Erkennung')
    sentimentbox = st.checkbox('Sentiment Analysis')

    st.write("---")
    if txt !="" and multiline == False:
        if zeroshotbox == True:
            with st.spinner('Zero-Shot-Classification wird durchgeführt...'):
                zeroshot = zeroshotNLP(txt)
            st.subheader(
            """
            Zero Shot Classification mit dem valhalla/distilbart-mnli-12-1 Modell:
            """
            )
            st.table(zeroshot)

        if hatespeachbox == True: 
            with st.spinner('Hate Speach Erkennung wird durchgeführt...'):
                hatespeach = hatespeachNLP(txt)
            st.subheader(
            """
            Hate Speach Erkennung mit dem Hate-speech-CNERG/dehatebert-mono-german Modell:
            """
            )
            st.write(hatespeach)

        if sentimentbox == True:
            with st.spinner('Sentiment Analysis wird durchgeführt...'):
                sentiment = sentimentNLP(txt)
            st.subheader(
            """
            Sentiment Analysis mit dem cardiffnlp/twitter-xlm-roberta-base-sentiment Modell:
            """
            )
            st.write(sentiment)

    elif txt != "" and multiline == True:
        st.write("Bitte gebe einen Text ein!")
    