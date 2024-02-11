from flask import Flask, Response
from bridges import magic_news, praza, reddit_switch

app = Flask(__name__)

@app.route("/")
def hello():
    return ":)"

@app.route("/magic_news")
def magic_news():
    txt = magic_news.rss()
    return Response(txt, mimetype="application/rss+xml")

@app.route("/praza")
def praza():
    txt = praza.rss()
    return Response(txt, mimetype="application/rss+xml")

@app.route("/reddit/NintendoSwitch")
def reddit_switch():
    txt = reddit_switch.rss()
    return Response(txt, mimetype="application/rss+xml")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
