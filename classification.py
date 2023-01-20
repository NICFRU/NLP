from transformers import pipeline, AutoTokenizer
import streamlit as st
import yaml
import pandas as pd


def load_yaml_file(file_path):
    # reads the yml files as a dictionary, were each topic is a key and the values are a list of elements
    with open(file_path, "r", encoding='UTF-8') as stream:
        yaml_dict = yaml.safe_load(stream)
        return yaml_dict



@st.cache(show_spinner=False)
def zeroshotNLP(text):
    topics = load_yaml_file('data/topic_g.yml')
    topic_list=[x.lower() for x in list(topics.keys())+['None']]
    zeroshot = pipeline("zero-shot-classification",
                      model="valhalla/distilbart-mnli-12-1")

    preddict = zeroshot(text, topic_list)

    return pd.DataFrame(preddict).drop("sequence",axis =1).head(3)


@st.cache(show_spinner=False)
def hatespeachNLP(text):
    hate_model_path = "Hate-speech-CNERG/dehatebert-mono-german"
    hate_task = pipeline(
        "text-classification", model=hate_model_path, tokenizer=hate_model_path
    )
    preddict = hate_task(text)[0]
    prob = round(preddict["score"],2)*100
    pred = preddict["label"]

    return f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell {pred} vorraus."

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

    return f"Mit einer Wahrscheinlichkeit von {prob}% sagt das Modell vorraus, dass dieser Text {pred} ist."
