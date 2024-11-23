# -*- coding: utf-8 -*-
"""
Created on Oct  26 19:53:42 2024

@author: roy62
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcom to flask'

#app.run(host='0.0.0.0', port=81)

app.run(host ='127.0.0.1', port=5000)

