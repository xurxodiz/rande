from flask import Flask, Response, render_template
from flask_caching import Cache
from bridges import MagicNews, Praza, reddit


app = Flask(__name__)

cache = Cache(config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 3600
})
cache.init_app(app)


@app.route("/")
def route_hello():
    return ":)"

@app.route("/magic_news")
@cache.cached()
def route_magic_news():
    return handler(MagicNews().feed_data())

@app.route("/praza")
@cache.cached()
def route_praza():
    return handler(Praza().feed_data())

@app.route("/r/NintendoSwitch")
@cache.cached()
def route_reddit_nintendo_switch():
    return handler(reddit.NintendoSwitch().feed_data())

@app.route("/r/truegaming")
@cache.cached()
def route_reddit_true_gaming():
    return handler(reddit.TrueGaming().feed_data())

def handler(data):
    txt = render_template("rss.xml", feed=data)
    return Response(txt, mimetype="text/xml")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
