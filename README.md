Rande
======

RSS bridges for websites without a feed. Named after the [Ponte de Rande](https://gl.wikipedia.org/wiki/Ponte_de_Rande).

Usage
-----

Create your own Python virtual environment (eg with `virtualenvwrapper`).

Activate it and install all dependencies: `pip install -r requirements.txt`.

You can then launch the Flask/Gunicorn application through PM2 (if you have it) by going running `pm2 start` from inside this folder.

It will be available in your browser in port 5000. If you are running Nginx, you may want to set up a reverse proxy.

Contents
--------

At the moment if offers four RSS bridges:

- Two scrapped from HTML:
  - `/magic_news` for https://magic.wizards.com/en/news
  - `/praza` for https://praza.gal/
- Two subreddits:
  - `/r/NintendoSwitch` for https://reddit.com/r/NintendoSwitch/
  - `/r/truegaming` for https://reddit.com/r/truegaming/