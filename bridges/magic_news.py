import requests
from lxml import etree

response = requests.get('https://magic.wizards.com/en/news')

parser = etree.HTMLParser()
root = etree.fromstring(response.text, parser)

def rss():
  r = """\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>Magic: the Gathering News</title>
  <link>https://magic.wizards.com/en/news</link>
  <description>Official news and articles for MtG.</description>
"""

  for article in root.iterfind(".//article"):

    r += "\t<item>\n"

    if (header := article.find(".//h3")) is not None:
        r += f"\t\t<title>{header.text}</title>\n"

    if (url := article.find(".//a[@data-link-type='router']")) is not None:
        r += f"\t\t<link>https://magic.wizards.com{url.get('href')}</link>\n"

    if (p := article.find(".//p")) is not None:
        desc = ''.join([p.text or ''] + [etree.tostring(e, encoding='unicode') for e in p])
        r += f"\t\t<description>{desc}</description>\n"

    r += "\t</item>\n"

  r += "</channel>\n</rss>\n"
  return r

if __name__ == "__main__":
   print(rss())