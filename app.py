from flask import Flask, Response, render_template
from flask_caching import Cache
from bridges import MagicWizardsCom


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

@app.route("/magic.wizards.com")
@cache.cached()
def route_magic_news():
    return handler(MagicWizardsCom().feed_data())

def handler(data):
    txt = render_template("rss.xml", feed=data)
    return Response(txt, mimetype="text/xml")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
