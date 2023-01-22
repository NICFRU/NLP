import streamlit as st
import pandas as pd
from classification import text_splitter, multi_line_zeroshotNLP, multi_line_hatespeechNLP, multi_line_sentimentNLP, multi_line_zeroshotNLP_V2,single_line_zeroshotNLP_V2,single_line_hatespeechNLP,single_line_sentimentNLP
from streamlit_toggle import st_toggle_switch
import streamlit as st


def show_predict_page():

    st.subheader(
    """
    NLP Modelle
    """
    )

    st.write(
    """
    Gib hier deinen Text ein:
    """
    )
    txt = st.text_area("Your text:",key= "NLP")

    colum1, colum2= st.columns(2)

    with colum1:
        zeroshotbox = st.checkbox('Zero Shot Klassifizierung')
        hatespeechbox = st.checkbox('Hate Speech Erkennung')
        sentimentbox = st.checkbox('Sentiment Analyse')


    with colum2:
        multiline = st_toggle_switch(
                                    label="Multi Line Text?",
                                    key="multiswitch",
                                    default_value=False,
                                    label_after=False,
                                    inactive_color="#D3D3D3",  # optional
                                    active_color="#11567f",  # optional
                                    track_color="#29B5E8",  # optional
                                )

    st.write("---")
    if txt !="" and multiline == False:
        if zeroshotbox == True:

            with st.spinner('Zero-Shot-Klassifizierung wird durchgeführt...'):
                zeroshot_plot = single_line_zeroshotNLP_V2(txt)
            st.subheader(
            """
            Zero Shot Klassifizierung mit dem valhalla/distilbart-mnli-12-1 Modell:
            """
            )
            st.plotly_chart(zeroshot_plot)

        if hatespeechbox == True: 
            with st.spinner('Hate Speech Erkennung wird durchgeführt...'):
                prob, pred, fig = single_line_hatespeechNLP(txt)

            st.subheader(
            """
            Hate Speech Erkennung mit dem Hate-speech-CNERG/dehatebert-mono-german Modell:
            """
            )
            st.write(f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell {pred} vorraus.")
            st.plotly_chart(fig)

        if sentimentbox == True:
            with st.spinner('Sentiment Analyse wird durchgeführt...'):
                    prob, pred,fig = single_line_sentimentNLP(txt)
            st.subheader(
            """
            Sentiment Analyse mit dem cardiffnlp/twitter-xlm-roberta-base-sentiment Modell:
            """
            )

            st.write(f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell vorraus, dass dieser Text {pred} ist.")
            st.plotly_chart(fig)





    elif txt != "" and multiline == True:
        
        sentlist = text_splitter(txt)

        if zeroshotbox == True:
            st.write(
            """
            ## Multi Text Zero Shot Klassifizierung mit dem valhalla/distilbart-mnli-12-1 Modell:
            """
            )
            with st.spinner('Zero Shot Klassifizierung wird durchgeführt...'):
                zfig = multi_line_zeroshotNLP(sentlist)
            st.write("### Plot welcher die Top 3 Preditcions zeigt:")
            st.plotly_chart(zfig)
            

            with st.spinner('Zero Shot Klassifizierung wird durchgeführt...'):
                zfig_v2 = multi_line_zeroshotNLP_V2(sentlist)
            
            st.write("### Plot welcher alle Scores der Preditcions der Labels zeigt:")
            st.plotly_chart(zfig_v2)

        if hatespeechbox == True:
            st.write(
            """
            ---
            ## Hate Speech Erkennung mit dem Hate-speech-CNERG/dehatebert-mono-german Modell:
            """
            )
            with st.spinner('Hate Speech Erkennung wird durchgeführt...'):
                hfig = multi_line_hatespeechNLP(sentlist)
            
            st.plotly_chart(hfig)

        if sentimentbox == True:
            st.write(
            """
            ---
            ## Multi Text Sentiment Analyse mit dem cardiffnlp/twitter-xlm-roberta-base-sentiment Modell
            """
            )
            with st.spinner('Sentiment Analyse wird durchgeführt...'):
                sfig = multi_line_sentimentNLP(sentlist)
            
            st.plotly_chart(sfig)