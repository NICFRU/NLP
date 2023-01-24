import streamlit as st

def select_page():
    st.markdown(
        """ 
        In diesem Frontend sind Visualisierungen unseres Projekts zu finden. Man kann sich Grafiken zu jeder Partei anzeigen lassen. \n
        Des weiteren ist es möglich sich Texte zusammenfassen zu lassen. Das ist hilfreich wenn man einen Abschnitt eines Parteiprogremmes zusammengefasst haben möchte. \n
        Im dritten Bereich dieses Frontends kann man folgende Modellierungen durchführen:
        - Zero-Shot-Klassifikation
            - Auswahl zwischen Spacy und Huggingface Modell
        - Hate-Speech Erkennung
        - Sentiment Analyse

        ---
        """
        )
    
    st.subheader("Meme of the project:")
    st.image("brace-yourself-nlp.jpg")
    st.caption("https://makeameme.org/meme/brace-yourself-nlp")