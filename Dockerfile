# app/Streamlit/NLP_Projekt

FROM python:3.7

WORKDIR /app

RUN git clone https://github.com/Coreprog/NLP-Frontend.git .

RUN pip3 install -r requirements.txt

RUN python -m spacy download de_core_news_lg

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"] 
