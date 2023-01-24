import streamlit as st
import pandas as pd
from classification import text_splitter, multi_line_zeroshotNLP, multi_line_hatespeechNLP, multi_line_sentimentNLP, multi_line_zeroshotNLP_V2,single_line_zeroshotNLP_V2,single_line_hatespeechNLP,single_line_sentimentNLP,spacy_model,multi_spacy_model
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

    colum1, colum2,colum3= st.columns(3)

    with colum1:
        zeroshotbox = st.checkbox('Zero Shot Klassifizierung')
        hatespeechbox = st.checkbox('Hate Speech Erkennung')
        sentimentbox = st.checkbox('Sentiment Analyse')

    with colum2:
        if zeroshotbox == True:
            pipe = st.radio(
                            "Welches Pipeline soll für die Zero Shot Klassifizierung genutzt werden:",
                            ('Huggingface', 'Spacy')
                            )


    with colum3:
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
            if pipe == "Huggingface":
                st.subheader(
                """
                Zero Shot Klassifizierung mit dem MoritzLaurer/mDeBERTa-v3-base-mnli-xnli Modell:
                """
                )

                with st.spinner('Zero-Shot-Klassifizierung wird durchgeführt...'):
                    zeroshot_plot = single_line_zeroshotNLP_V2(txt)

                st.plotly_chart(zeroshot_plot)
            
            elif pipe == "Spacy":
                st.subheader(
                """
                Zero Shot Klassifizierung mit dem de_core_news_lg Modell:
                """
                )

                with st.spinner('Zero Shot Klassifizierung wird durchgeführt...'):
                    fig = spacy_model(txt)

                st.plotly_chart(fig)


        if hatespeechbox == True: 

            st.subheader(
            """
            Hate Speech Erkennung mit dem Hate-speech-CNERG/dehatebert-mono-german Modell:
            """
            )

            with st.spinner('Hate Speech Erkennung wird durchgeführt...'):
                prob, pred, fig = single_line_hatespeechNLP(txt)

            st.write(f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell {pred} vorraus.")
            st.plotly_chart(fig)

        if sentimentbox == True:

            st.subheader(
            """
            Sentiment Analyse mit dem cardiffnlp/twitter-xlm-roberta-base-sentiment Modell:
            """
            )

            with st.spinner('Sentiment Analyse wird durchgeführt...'):
                    prob, pred,fig = single_line_sentimentNLP(txt)


            st.write(f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell vorraus, dass dieser Text {pred} ist.")
            st.plotly_chart(fig)





    elif txt != "" and multiline == True:
        
        sentlist = text_splitter(txt)

        if zeroshotbox == True:
            if pipe == "Huggingface":
                st.subheader(
                """
                Multi Text Zero Shot Klassifizierung mit dem MoritzLaurer/mDeBERTa-v3-base-mnli-xnli Modell:
                """
                )
                

                with st.spinner('Zero Shot Klassifizierung wird durchgeführt...'):
                    zfig_v2 = multi_line_zeroshotNLP_V2(sentlist)
                
                st.plotly_chart(zfig_v2)
            
            elif pipe == "Spacy":

                st.subheader(
                """
                Multi Text Zero Shot Klassifizierung mit dem de_core_news_lg Modell:
                """
                )

                with st.spinner('Zero Shot Klassifizierung wird durchgeführt...'):
                    fig_v2  = multi_spacy_model(sentlist)

                st.plotly_chart(fig_v2)

        if hatespeechbox == True:
            st.subheader(
            """
            Multi Text Hate Speech Erkennung mit dem Hate-speech-CNERG/dehatebert-mono-german Modell:
            """
            )
            with st.spinner('Hate Speech Erkennung wird durchgeführt...'):
                hfig = multi_line_hatespeechNLP(sentlist)
            
            st.plotly_chart(hfig)

        if sentimentbox == True:
            st.subheader(
            """
             Multi Text Sentiment Analyse mit dem cardiffnlp/twitter-xlm-roberta-base-sentiment Modell:
            """
            )
            with st.spinner('Sentiment Analyse wird durchgeführt...'):
                sfig = multi_line_sentimentNLP(sentlist)
            
            st.plotly_chart(sfig)