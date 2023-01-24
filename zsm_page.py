import streamlit as st
from summarization import summarize_text


def show_nlp_zsmf():

    st.subheader(
    """
    NLP Zusammenfasser
    """
    )
    colum11, colum22= st.columns([8,1])
    with colum11:
        text = st.text_area("Text für Zusammenfassung:",key= "SUM")

    with colum22:
        num = st.number_input("Anzahl zsmgf. Sätze ", value = 0, step = 1, min_value = 0, max_value=75)

    if text != "" and num != 0:
        sum = summarize_text(text,num)
        st.subheader("Ihre Zusammenfassung:")
        st.write(sum)
    else:
        pass
