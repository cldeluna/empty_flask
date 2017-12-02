#!/usr/bin/python -tt
# Project: empty_flask
# Filename: headlines.py
# claud
# PyCharm

from __future__ import absolute_import, division, print_function

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "12/2/2017"
__copyright__ = "Copyright (c) 2016 Claudia"
__license__ = "Python"

import os
import argparse
import feedparser
from flask import Flask, render_template

app = Flask(__name__)


RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'ansible': 'http://news.ansible.uk/rss.xml'}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):

  feed = feedparser.parse(RSS_FEEDS[publication])

  return render_template("home.html", article=feed['entries'])

if __name__ == "__main__":
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True

    app.run(host=host, port=port, debug=True)



