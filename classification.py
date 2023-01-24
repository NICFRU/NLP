from transformers import pipeline, AutoTokenizer
import streamlit as st
import yaml
import pandas as pd
import re
import plotly.express as px
from transformers import AutoTokenizer,AutoConfig,AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np


def load_yaml_file(file_path):
    # reads the yml files as a dictionary, were each topic is a key and the values are a list of elements
    with open(file_path, "r", encoding='UTF-8') as stream:
        yaml_dict = yaml.safe_load(stream)
        return yaml_dict


# Huggingface

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
                      model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")

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
                      model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")

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
                      model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")

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




# Spacy

import spacy
#!python -m spacy download de_core_news_lg

def load_model():
    return spacy.load("de_core_news_lg",disable=['parser', 'ner','tagger'])

from string import punctuation
import re

def _add_sentence_to_list(sentence: str, sentences_list):
    """
    Add a sentence to the list of sentences.
    Args:
        sentence (str):
            Sentence to be added.
        sentences (List[str]):
            List of sentences.
    """
    while sentence.startswith(" "):
        # remove leading space
        sentence = sentence[1:]
    if all(c in punctuation for c in sentence) or len(sentence) == 1:
        # skip sentences with only punctuation
        return
    sentences_list.append(sentence)

def get_sentences(text: str):
    """
    Get sentences from a text.
    Args:
        text (str):
            Text to be processed.
    Returns:
        List[str]:
            List of sentences.
    """
    # get the paragraphs
    text=   re.sub(" \d+\n", ".", text)
    text=   re.sub("\n\d+", " ", text)
    text=   re.sub("\n", " ", text)
    text=   re.sub("\d+.", "", text)
    paragraphs = re.split(r' *[\.\?!][\'"\)\]]* *', text)
    paragraphs = [p for p in paragraphs if p != ""]
    # get the sentences from the paragraphs
    sentences = list()
    for paragraph in paragraphs:
        if paragraph.startswith("#"):
            _add_sentence_to_list(paragraph, sentences)
            continue
        prev_sentence_idx = 0
        for idx in range(len(paragraph)):
            if idx + 1 < len(paragraph):
                if (paragraph[idx] == "." and not paragraph[idx + 1].isdigit()) or (
                    paragraph[idx] in "!?"
                ):
                    sentence = paragraph[prev_sentence_idx : idx + 1]
                    _add_sentence_to_list(sentence, sentences)
                    prev_sentence_idx = idx + 1
            else:
                sentence = paragraph[prev_sentence_idx:]
                _add_sentence_to_list(sentence, sentences)
    return sentences



def get_topical_sentences(
    sentences, topics, df_y=0
) :

    "classifies the content based on the frequency of the occurring words of the classes"
    sent_df=[]
    topical_sentences = dict()
    topics_list=[]
    for topic in topics:
        topics_list.append(topic)
        topical_sentences[topic] = list()
        #topical_sentences[f'{topic}_num'] = list()
    for sentence in sentences:
        topic_list=[]
        for topic in topics:
            topic_num = 0
            if any(str(topical_word) in str(sentence.lower()) for topical_word in topics[topic]):
                for  topical_word in topics[topic]:
                        if str(topical_word) in str(sentence.lower()):
                            topic_num+=1
                
                
            else:
                topic_num=0
            topic_list.append(topic_num)
        
        topical_sentences[topics_list[max(range(len(topic_list)), key=topic_list.__getitem__)]].append(sentence)
        if df_y:
            sent_df.append([sentence,topics_list[max(range(len(topic_list)), key=topic_list.__getitem__)],topic_list,topics_list])
    if df_y:
        return pd.DataFrame(data=sent_df,columns=['text','pred',"score","labels"])

    return topical_sentences




def text_lemma(lsit,nlp):
    liste=[]
    doc = nlp(lsit)
    for token in doc:
        if not token.is_stop and not token.is_punct:
            liste.append(token.lemma_.lower())

    return ' '.join(liste)

def list_lemma(lsit,nlp):
    liste=[]
    string=' '.join(lsit)
    nlp = spacy.load("de_core_news_lg")
    doc = nlp(str(string))
    for token in doc:
        if not token.is_stop and not token.is_punct:
            liste.append(token.lemma_.lower())
    return list(dict.fromkeys(liste)) 

@st.cache(show_spinner=False)
def spacy_model(text):
    topics = load_yaml_file('data/topic_g.yml')
    nlp = load_model()
    for topic in topics.keys():
        topics[topic]=list_lemma(topics[topic],nlp)
    sent = []
    sent.append(text_lemma(text,nlp))
    df = get_topical_sentences(sent, topics,1)
    fig_df = pd.DataFrame().from_dict({"Prediction":list(df["labels"])[0],"Score":list(df["score"][0])})
    fig = px.bar(fig_df, x="Prediction", y="Score",color="Prediction")
    return fig

@st.cache(show_spinner=False)
def multi_spacy_model(sentlist):
    topics = load_yaml_file('data/topic_g.yml')
    nlp = load_model()
    for topic in topics.keys():
        topics[topic]=list_lemma(topics[topic],nlp)
    sent = []
    for text in sentlist:
        sent.append(text_lemma(text,nlp))
    df = get_topical_sentences(sent, topics,1)
    fig_df = pd.DataFrame().from_dict({"Prediction":list(df["labels"])[0],"Score":[sum(i) for i in zip(*df.score)]})
    fig = px.bar(fig_df, x="Prediction", y="Score",color="Prediction")
    return fig