from transformers import pipeline, AutoTokenizer
import streamlit as st
import yaml
import pandas as pd
import re
import plotly.express as px


def load_yaml_file(file_path):
    # reads the yml files as a dictionary, were each topic is a key and the values are a list of elements
    with open(file_path, "r", encoding='UTF-8') as stream:
        yaml_dict = yaml.safe_load(stream)
        return yaml_dict

@st.cache(show_spinner=False)
def text_splitter(text):
    text=   re.sub(" \d+\n", ".", text)
    text=   re.sub("\n\d+", " ", text)
    text=   re.sub("\n", " ", text)
    
    return re.split(r' *[\.\?!][\'"\)\]]* *', text)[:-1]


@st.cache(show_spinner=False)
def zeroshotNLP(text):
    topics = load_yaml_file('data/topic_g.yml')
    topic_list=[x.lower() for x in list(topics.keys())+['None']]
    zeroshot = pipeline("zero-shot-classification",
                      model="valhalla/distilbart-mnli-12-1")

    preddict = zeroshot(text, topic_list)
    df = pd.DataFrame(preddict).drop("sequence",axis =1).head(3)
    df = df.rename({"scores":"Score","labels":"Prediction"},axis="columns")

    return df


@st.cache(show_spinner=False)
def hatespeechNLP(text):
    hate_model_path =  "deepset/bert-base-german-cased-hatespeech-GermEval18Coarse" #"Hate-speech-CNERG/dehatebert-mono-german"
    hate_task = pipeline(
        "text-classification", model=hate_model_path, tokenizer=hate_model_path
    )

    #"deepset/bert-base-german-cased-hatespeech-GermEval18Coarse"

    preddict = hate_task(text)[0]
    prob = round(preddict["score"],2)*100
    pred = preddict["label"]

    return prob,pred

@st.cache(show_spinner=False)
def sentimentNLP(text):
    sentiment_model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
    tokenizer=AutoTokenizer.from_pretrained("cardiffnlp/twitter-xlm-roberta-base-sentiment",use_fast=False)
    sentiment_task = pipeline(
        "sentiment-analysis", model=sentiment_model_path, tokenizer=tokenizer
    )

    preddict = sentiment_task(text)[0]
    prob = round(preddict["score"],2)*100
    pred = preddict["label"]

    return prob, pred

@st.cache(show_spinner=False)
def multi_line_zeroshotNLP(sentlist):
    ergebnis = [zeroshotNLP(sent) for sent in sentlist]
    df = pd.concat(ergebnis).reset_index()
    df = df.rename({"index":"Place"}, axis='columns')
    df["Place"] = df["Place"].replace(0,"Place 1")
    df["Place"] = df["Place"].replace(1,"Place 2")
    df["Place"] = df["Place"].replace(2,"Place 3")
    fig = px.bar(df, x="Place", y="Score", color="Prediction")
    
    return fig

@st.cache(show_spinner=False)
def multi_line_hatespeechNLP(sentlist):
    ergebnis = [hatespeechNLP(sent) for sent in sentlist]
    df = pd.DataFrame(ergebnis, columns = ["Score", "Prediction"])
    fig = px.bar(df, x="Prediction", y="Score",color="Prediction")
    return fig

@st.cache(show_spinner=False)
def multi_line_sentimentNLP(sentlist):
    ergebnis = [sentimentNLP(sent) for sent in sentlist]
    df = pd.DataFrame(ergebnis, columns = ["Score", "Prediction"])
    fig = px.bar(df, x="Prediction", y="Score",color="Prediction")
    return fig



@st.cache(show_spinner=False)
def zeroshotNLP_V2(text):
    topics = load_yaml_file('data/topic_g.yml')
    topic_list=[x.lower() for x in list(topics.keys())+['None']]
    zeroshot = pipeline("zero-shot-classification",
                      model="valhalla/distilbart-mnli-12-1")

    preddict = zeroshot(text, topic_list)
    df = pd.DataFrame(preddict).drop("sequence",axis =1)
    df = df.rename({"scores":"Score","labels":"Prediction"},axis="columns")

    return df


@st.cache(show_spinner=False)
def multi_line_zeroshotNLP_V2(sentlist):
    ergebnis = [zeroshotNLP_V2(sent) for sent in sentlist]
    df = pd.concat(ergebnis)
    fig = px.bar(df, x="Prediction", y="Score",color="Prediction")
    return fig


@st.cache(show_spinner=False)
def single_line_zeroshotNLP_V2(text):
    topics = load_yaml_file('data/topic_g.yml')
    topic_list=[x.lower() for x in list(topics.keys())+['None']]
    zeroshot = pipeline("zero-shot-classification",
                      model="valhalla/distilbart-mnli-12-1")

    preddict = zeroshot(text, topic_list)
    df = pd.DataFrame(preddict).drop("sequence",axis =1)
    df = df.rename({"scores":"Score","labels":"Prediction"},axis="columns")
    fig = px.bar(df, x="Prediction", y="Score",color="Prediction")

    return fig

@st.cache(show_spinner=False)
def single_line_hatespeechNLP(text):
    hate_model_path = "deepset/bert-base-german-cased-hatespeech-GermEval18Coarse"
    hate_task = pipeline(
        "text-classification", model=hate_model_path, tokenizer=hate_model_path
    )
    preddict = hate_task(text)[0]
    prob = round(preddict["score"]*100,2)
    pred = preddict["label"]
    notprob = 100 - prob
    if pred == "OFFENSE":
        notpred = "OTHER"
    elif pred == "OTHER":
        notpred = "OFFENSE"
    df = pd.DataFrame.from_dict({"Label":[pred,notpred],"Score":[prob,notprob]})
    fig = px.bar(df, x="Label", y="Score",color="Label")

    return prob, pred, fig

from transformers import AutoTokenizer,AutoConfig,AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np


@st.cache(show_spinner=False)
def single_line_sentimentNLP(text):
    MODEL = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)


    model = AutoModelForSequenceClassification.from_pretrained(MODEL)

    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    l = []
    s = []
    for i in range(scores.shape[0]):
        l.append(config.id2label[ranking[i]])
        s.append(round(scores[ranking[i]]*100,2))

    df = pd.DataFrame.from_dict({"Label":l,"Score":s})
    fig = px.bar(df, x="Label", y="Score",color="Label")
    prob = s[0]
    pred = l[0]

    return prob, pred, fig

