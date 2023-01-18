#%%
import os

DATA_DIR='data/raw'
data_names = os.listdir(DATA_DIR)
data_names = [name[:-4] for name in data_names if name != ".DS_Store"]

#%%
import yaml

def load_yaml_file(file_path):
    # reads the yml files as a dictionary, were each topic is a key and the values are a list of elements
    with open(file_path, "r", encoding='UTF-8') as stream:
        yaml_dict = yaml.safe_load(stream)
        return yaml_dict

topics = load_yaml_file('topic_modeling/topic_g.yml')

#%%
from string import punctuation
import re

def load_markdown_file(file_path):
    with open(file_path, "r", encoding='UTF-8') as stream:
        markdown_str = stream.read()
        return markdown_str

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

#%%
from transformers import pipeline
import pandas as pd
from tqdm import tqdm
pd.options.mode.chained_assignment = None

classifier = pipeline("zero-shot-classification",
                      model="valhalla/distilbart-mnli-12-1")

topic_list=[x.lower() for x in list(topics.keys())+['None']]

for element in list(filter(None, data_names)):
    print(element)
    df_topic = pd.DataFrame()
    program_txt = load_markdown_file(f"{DATA_DIR}/{element}.txt")
    sentences = get_sentences(program_txt)

    for sentence in tqdm(sentences):
        x = classifier(sentence, topic_list)
        df = pd.DataFrame.from_dict(x)
        row = df.iloc[0]
        row["Top 3"] = [tuple(x) for x in df[["labels","scores"]].head(3).to_records(index=False)]
        df_topic = df_topic.append(row)  
    df_topic.to_csv(f"{element}_topicpred_valhalla.csv")
    