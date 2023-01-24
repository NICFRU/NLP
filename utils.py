import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px


def html_reader(name):
    HtmlFile = open(name, 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    return components.html(source_code,height = 450)





# Plot Generation

@st.cache(show_spinner=False)
def getbarchalleparteienhuggingface(): 
    data=pd.read_csv("plotcsv/aggrmDeBERTa.csv", sep=";")
    fig = px.bar(data, x='Topic', y='Score', color="Partei", text="Anteil", title="Topicverteilung für alle Parteien (huggingface)")
    return fig

@st.cache(show_spinner=False)
def getbarcheinzelparteihuggingface(partei):
    datapre=pd.read_csv("plotcsv/aggrmDeBERTa.csv", sep=";")
    data=datapre[datapre["Partei"]==partei].copy()
    fig = px.bar(data, x='Topic', y='Score', text="Score", title="Topicverteilung für die "+partei+" (huggingface)")
    return fig

@st.cache(show_spinner=False)
def getbarchalleparteientopic_class():
    data=pd.read_csv("plotcsv/aggrtopic_classtopicdata.csv", sep=";")
    fig = px.bar(data, x='Topic', y='Score', color="Partei", text="Anteil", title="Topicverteilung für alle Parteien (spacy)")
    return fig



@st.cache(show_spinner=False)
def getbarcheinzelparteitopic_class(partei):
    datapre=pd.read_csv("plotcsv/aggrtopic_classtopicdata.csv", sep=";")
    data=datapre[datapre["Partei"]==partei].copy()
    fig = px.bar(data, x='Topic', y='Score', text="Score", title="Topicverteilung für die "+partei+" (spacy)")
    return fig
