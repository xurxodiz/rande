from flask import Flask, Response
from bridges import magic_news, praza, reddit_switch

app = Flask(__name__)

@app.route("/")
def route_hello():
    return ":)"

@app.route("/magic_news")
def route_magic_news():
    txt = magic_news.rss()
    return Response(txt, mimetype="application/rss+xml")

@app.route("/praza")
def route_praza():
    txt = praza.rss()
    return Response(txt, mimetype="application/rss+xml")

@app.route("/reddit/NintendoSwitch")
def route_reddit_switch():
    txt = reddit_switch.rss()
    return Response(txt, mimetype="application/rss+xml")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
