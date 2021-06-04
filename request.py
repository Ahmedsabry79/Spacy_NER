#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:50:07 2021

@author: ahmed
"""

import requests

result_1 = requests.post("http://0.0.0.0:5000/get_available_entities", 
                         )

result_2 = requests.post("http://0.0.0.0:5000/get_entities", 
                         json = {"text": "Ahmed Sabry and Mohammed are in Cairo."})

eval(result_2.text)['result']
