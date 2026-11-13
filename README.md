Rande
======

RSS bridges for websites without a feed. Named after the [Ponte de Rande](https://gl.wikipedia.org/wiki/Ponte_de_Rande).

Usage
-----

Install dependencies with `uv sync`.

You can then launch the Flask/Gunicorn application through PM2 (if you have it) by going running `pm2 start` from inside this folder.

It will be available in your browser in port 5000. If you are running Nginx, you may want to set up a reverse proxy.

Contents
--------

At the moment if offers just one RSS bridge:

- Scrapped from HTML:
  - `/magic.wizards.com` for https://magic.wizards.com/en/news
