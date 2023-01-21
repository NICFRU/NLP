import streamlit as st
import pandas as pd
from classification import zeroshotNLP, hatespeachNLP, sentimentNLP, text_splitter, multi_line_zeroshotNLP, multi_line_hatespeachNLP, multi_line_sentimentNLP, multi_line_zeroshotNLP_V2
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
                prob, pred= hatespeachNLP(txt)
            st.subheader(
            """
            Hate Speach Erkennung mit dem Hate-speech-CNERG/dehatebert-mono-german Modell:
            """
            )
            st.write(f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell {pred} vorraus.")

        if sentimentbox == True:
            with st.spinner('Sentiment Analysis wird durchgeführt...'):
                prob, pred = sentimentNLP(txt)
            st.subheader(
            """
            Sentiment Analysis mit dem cardiffnlp/twitter-xlm-roberta-base-sentiment Modell:
            """
            )
            st.write(f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell vorraus, dass dieser Text {pred} ist.")

    elif txt != "" and multiline == True:
        
        sentlist = text_splitter(txt)

        if zeroshotbox == True:
            with st.spinner('Zero Shot Classification wird durchgeführt...'):
                zfig = multi_line_zeroshotNLP(sentlist)
            st.subheader(
            """
            Multi Text Zero Shot Classification mit dem valhalla/distilbart-mnli-12-1 Modell:
            """
            )
            st.plotly_chart(zfig)

            st.subheader("oder")

            with st.spinner('Zero Shot Classification wird durchgeführt...'):
                zfig_v2 = multi_line_zeroshotNLP_V2(sentlist)
            st.subheader(
            """
            Multi Text Zero Shot Classification mit dem valhalla/distilbart-mnli-12-1 Modell:
            """
            )
            st.plotly_chart(zfig_v2)

        if hatespeachbox == True:
            with st.spinner('Hate Speach Erkennung wird durchgeführt...'):
                hfig = multi_line_hatespeachNLP(sentlist)
            st.subheader(
            """
            Hate Speach Erkennung mit dem Hate-speech-CNERG/dehatebert-mono-german Modell:
            """
            )
            st.plotly_chart(hfig)

        if sentimentbox == True:
            with st.spinner('Sentiment Analysis wird durchgeführt...'):
                sfig = multi_line_sentimentNLP(sentlist)
            st.subheader(
            """
            Multi Text Sentiment Analysis mit dem cardiffnlp/twitter-xlm-roberta-base-sentiment Modell
            """
            )
            st.plotly_chart(sfig)