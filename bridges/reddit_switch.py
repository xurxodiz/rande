from datetime import datetime
import json
import html
import requests

response = requests.get('https://www.reddit.com/r/NintendoSwitch.json')
data = json.loads(response.text)

def rss():
  r = """\
<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>Reddit - Nintendo Switch</title>
  <link>https://reddit.com/r/NintendoSwitch/</link>
  <description>The central hub for all news, updates, rumors, and topics relating to the Nintendo Switch. We are a fan-run community, not an official Nintendo forum..</description>
"""

  for pt in data["data"]["children"]:
    post = pt["data"]

    r += "\t<item>\n"

    r += f"\t\t<pubDate>{datetime.fromtimestamp(post['created'])}</pubDate>\n"

    r += f"\t\t<title>{post['title']}</title>\n"
    r += f"\t\t<link>https://reddit.com{post['permalink']}</link>\n"

    if post["selftext_html"]:
      r += f"\t\t<description>{html.unescape(post['selftext_html'])}</description>\n"

    if post["thumbnail"] != "self":
      r += f"\t\t<media:thumbnail url=\"{post['thumbnail']}\" />\n"

    r += "\t</item>\n"

  r += "</channel>\n</rss>\n"
  return r

if __name__ == "__main__":
   print(rss())