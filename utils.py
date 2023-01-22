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
def getreltopicscore(inputdf):
    inputdf["Anteil"]=0
    for i in inputdf["Topic"].unique():
        for j in inputdf[inputdf["Topic"]==i].index:
            inputdf["Anteil"][j] = round(inputdf["Score"][j]/inputdf[inputdf["Topic"]==i]["Score"].sum(), 4)
    return inputdf



@st.cache(show_spinner=False)
def getbarchalleparteienvalhalla(): 
    data=pd.read_csv("plotcsv/aggrvalhallatopicdata.csv", sep=";")
    data=getreltopicscore(data).copy()
    fig = px.bar(data, x='Topic', y='Score', color="Partei", text="Anteil", title="Topicverteilung für alle Parteien (Valhalla)")
    return fig

@st.cache(show_spinner=False)
def getbarcheinzelparteivalhalla(partei):
    datapre=pd.read_csv("plotcsv/aggrvalhallatopicdata.csv", sep=";")
    data=datapre[datapre["Partei"]==partei].copy()
    fig = px.bar(data, x='Topic', y='Score', text="Score", title="Topicverteilung für die "+partei+" (Valhalla)")
    return fig

@st.cache(show_spinner=False)
def getbarchalleparteientopic_class():
    data=pd.read_csv("plotcsv/aggrtopic_classtopicdata.csv", sep=";")
    data=getreltopicscore(data).copy()
    fig = px.bar(data, x='Topic', y='Score', color="Partei", text="Anteil", title="Topicverteilung für alle Parteien (topic_class)")
    return fig



@st.cache(show_spinner=False)
def getbarcheinzelparteitopic_class(partei):
    datapre=pd.read_csv("plotcsv/aggrtopic_classtopicdata.csv", sep=";")
    data=datapre[datapre["Partei"]==partei].copy()
    fig = px.bar(data, x='Topic', y='Score', text="Score", title="Topicverteilung für die "+partei+" (topic_class)")
    return fig
