import streamlit as st
from utils import  html_reader,getbarchalleparteienvalhalla,getbarcheinzelparteivalhalla,getbarchalleparteientopic_class,getbarcheinzelparteitopic_class


def show_explore_page():
    st.write("## Graphische Analyse der Ergbnisse")

    st.write(
        """
     ### Gebe die Partei an für die die Grafiken geladen werden sollen.
    """
    )


    
    menu = ["--select--","AFD","CDU-CSU","GRUENE","LINKE","FDP","SPD"]
    PTR = st.selectbox("Auswahl der Partei:", menu)
    
    if PTR == "--select--":
        pass
    else:        
        colums1, colums2= st.columns(2)

        with colums1:
            st.plotly_chart(getbarcheinzelparteivalhalla(PTR))

        with colums2:
            st.plotly_chart(getbarcheinzelparteitopic_class(PTR))

        col1, col2, col3= st.columns([1,3,1])
        with col1:
            st.write(" ")

        with col2:
            st.image(f"words/{PTR}_most_words.jpg",width=800)

        with col3:
            st.write(" ")

    st.write("---")
    st.write(
        """
     ### Hatespeech-Vergleich aller Parteien
    """
    )
    colum1, colum2= st.columns(2)

    with colum1:
        st.plotly_chart(getbarchalleparteienvalhalla())
        html_reader("data/Hatespeechvergleich-je-Partei.html")

    with colum2:
        st.plotly_chart(getbarchalleparteientopic_class())
        html_reader("data/Hatespeechvergleich-je-Partei-und-Themengebiet.html")

    
