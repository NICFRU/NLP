import streamlit as st
import pandas as pd
from classification import zeroshotNLP, hatespeachNLP, sentimentNLP

def show_predict_page_1():
    st.subheader(
    """
    Das ist die Topic Prediction von Texten. Gebe in das untenliegende Feld deinen Text ein.
    """
    )
    txt = st.text_area("Your text:")

    st.write(
    """
    Gib hier deinen Text ein:
    """
    )

    

    zeroshotbox = st.checkbox('Zero Shot Calssification')
    hatespeachbox = st.checkbox('Hate Speach Erkennung')
    sentimentbox = st.checkbox('Sentiment Analysis')

    if txt !="":
        
        if zeroshotbox == True:
            zeroshot = zeroshotNLP(txt)
            st.subheader(
            """
            Zero Shot Calssification mit dem valhalla/distilbart-mnli-12-1 Modell:
            """
            )

            st.table(zeroshot)
        if hatespeachbox == True: 
            hatespeach = hatespeachNLP(txt)
            st.subheader(
            """
            Hate Speach Erkennung mit dem Hate-speech-CNERG/dehatebert-mono-german Modell:
            """
            )
            st.write(hatespeach)

        if sentimentbox == True:
            sentiment = sentimentNLP(txt)
            st.subheader(
            """
            Sentiment Analysis mit dem cardiffnlp/twitter-xlm-roberta-base-sentiment Modell:
            """
            )
            st.write(sentiment)

    else:
        st.write("Bitte gebe einen Text ein!")
    