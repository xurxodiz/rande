import json

data = json.load('https://www.reddit.com/r/NintendoSwitch.json')

def rss():
  r = """\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>Praza Pública</title>
  <link>https://praza.gal/</link>
  <description>O xornal da Galicia que vén.</description>
"""

  for post in data["data"]["children"]:

    r += "\t<item>\n"

    if (dt := article.find(".//time[@datetime]")) is not None:
       r += f"\t\t<pubDate>{dt.get('datetime')}</pubDate>\n"

    if (header := article.find(".//h2")) is not None:
        if (a := header.find(".//a")) is not None:
          r += f"\t\t<title>{a.text}</title>\n"
          r += f"\t\t<link>https://praza.gal{a.get('href')}</link>\n"

    if (p := article.find(".//p")) is not None:
        desc = ''.join([p.text or ''] + [etree.tostring(e, encoding='unicode') for e in p])
        r += f"\t\t<description>{desc}</description>\n"

    if (img := article.find(".//img[@class='article-summary-image']")) is not None:
       r += f"\t\t<media:thumbnail url=\"{img.get('src')}\" />\n"

    r += "\t</item>\n"

  r += "</channel>\n</rss>\n"
  return r

if __name__ == "__main__":
   print(rss())