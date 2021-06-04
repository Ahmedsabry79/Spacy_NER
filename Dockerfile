From python:3.8
USER root
RUN apt-get update
COPY . /spacy_ner_model
WORKDIR spacy_ner_model
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_sm
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "wsgi:app"]
EXPOSE 5000
