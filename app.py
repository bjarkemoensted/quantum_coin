#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 15:27:24 2018

@author: ahura
"""

import datetime
from flask import Flask, render_template, flash, request, session, redirect
import urllib.request

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'DGD463463etrhSDGHSdfhsd3t34ERGSDFg'

def get_bin():
    d = {49: 1, 48: 0}
    x = urllib.request.urlopen("https://qrng.anu.edu.au/ran_bin.php").read()
    int_ = d[list(x)[0]]
    return int_

@app.route("/")
def index():

    r = get_bin()

    if r == 0:
        return "Kamilla"
    else:
        return "Bjarke"


if __name__ == "__main__":
    app.run()