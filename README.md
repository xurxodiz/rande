Rande
======

RSS bridges for websites without a feed. Named after the [Ponte de Rande](https://gl.wikipedia.org/wiki/Ponte_de_Rande).

Usage
-----

Install dependencies with `uv sync`.

Then you can run `supervisord` in this folder and gunicorn/flask will do the rest.

It will be available in your browser in port 5000. If you are running Nginx, you may want to set up a reverse proxy.

If you want to ensure it is restarted after reboots, run `crontab -e` and add this:

```
@reboot cd /path/to/rande && supervisord
```

Contents
--------

At the moment if offers just one RSS bridge:

- Scrapped from HTML:
  - `/magic.wizards.com` for https://magic.wizards.com/en/news
