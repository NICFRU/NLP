import streamlit as st
import streamlit.components.v1 as components



def html_reader(name):
    HtmlFile = open(name, 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    return components.html(source_code,height = 450)

