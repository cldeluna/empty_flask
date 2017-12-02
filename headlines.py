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

import argparse
import feedparser
from flask import Flask

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def get_news():
  feed = feedparser.parse(BBC_FEED)
  first_article = feed['entries'][0]
  return """<html>
    <body>
        <h1> BBC Headlines </h1>
        <b>{0}</b> <br/>
        <i>{1}</i> <br/>
        <p>{2}</p> <br/>
    </body>
</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == "__main__":
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True

    app.run(host=host, port=port)



