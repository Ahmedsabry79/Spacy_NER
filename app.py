#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:17:31 2021

@author: asabry
"""

import spacy
from flask import Flask, jsonify, request

app = Flask(__name__)
    
nlp = spacy.load("en_core_web_sm")

@app.route("/get_entities", methods = ['POST'])
def get_entities():
    if request.method == 'POST':
        try:
            doc = request.json['text']
            doc = nlp(doc)
            ents_dict = {}
            for doc_ent in doc.ents:
                ents_dict[str(doc_ent.text)] = str(doc_ent.label_)
            success = "true"
        except:
            success = "false"
        return jsonify({"success": success,
                        "result":ents_dict})
    else:
        return jsonify({"success": "false",
                        "result": {}})

@app.route("/get_available_entities", methods = ['POST'])
def get_available_entities():
    if request.method == 'POST':
        success = "true"
        entities = ['Geographical Entity',
                    'Organization',
                    'Person',
                    'Geopolitical Entity',
                    'Time indicator',
                    'Artifact',
                    'Event',
                    'Natural Phenomenon']
        
        return jsonify({"success": success,
                        "result":entities})
    else:
        return jsonify({"success": "false",
                        "result": []})

if __name__ == '__main__':
    app.run("0.0.0.0:5000", debug=False)