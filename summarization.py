from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import re
import nltk
import streamlit as st

nltk.download('punkt')

@st.cache(show_spinner=False)
def summarize_text(text, sentence_count, ignore_sentences=[]):
    summarizer = TextRankSummarizer()
 
    def change_text(text, additionals=[]):
        text = re.sub(" \d+\n", ".", text)
        text = re.sub("\n\d+", " ", text)
        text = re.sub("\n", " ", text)
        text = re.sub("- ", "", text)
        text = re.sub("[0-9]", "", text)
        text = re.sub("()", "", text)
        for entry in additionals:
            text = re.sub(entry, "", text)
        sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
        return sentences
    
    def list_to_string(liste):
        sentence_string = ""
        for elem in liste:
            sentence_string += elem
            sentence_string += ". "
        return sentence_string

    changed_text = change_text(text, ignore_sentences)
    parser = PlaintextParser.from_string(list_to_string(changed_text), Tokenizer("german"))
    summary = summarizer(parser.document, sentence_count)
    text_summary = ""
    for sentence in summary:
        text_summary += str(sentence)
    return text_summary
    