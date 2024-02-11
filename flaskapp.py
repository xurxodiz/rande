from flask import Flask, Response
from magic_news import rss as magic_news_rss
from praza import rss as praza_rss
from reddit_switch import rss as reddit_switch_rss

app = Flask(__name__)

@app.route("/")
def hello():
    return ":)"

@app.route("/magic_news")
def magic_news():
    txt = magic_news_rss()
    return Response(txt, mimetype="application/rss+xml")

@app.route("/praza")
def praza():
    txt = praza_rss()
    return Response(txt, mimetype="application/rss+xml")

@app.route("/reddit/NintendoSwitch")
def reddit_switch():
    txt = reddit_switch_rss()
    return Response(txt, mimetype="application/rss+xml")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
