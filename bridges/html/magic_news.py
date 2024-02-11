from lxml import etree

from .html_feed import HtmlFeed

class MagicNews(HtmlFeed):

  def __init__(self):
    super().__init__('https://magic.wizards.com/en/news')

  def feed_data(self):
    data = {
      "title": "Magic: the Gathering News",
      "link": "https://magic.wizards.com/en/news",
      "description": "Official news and articles for MtG.",
      "itemlist": []
    }

    for article in self.root.iterfind(".//article"):

      item = {}

      if (header := article.find(".//h3")) is not None:
          item["title"] = header.text

      if (url := article.find(".//a[@data-link-type='router']")) is not None:
          item["link"] = f"https://magic.wizards.com{url.get('href')}"

      if (p := article.find(".//p")) is not None:
          item["description"] = ''.join([p.text or ''] + [etree.tostring(e, encoding='unicode') for e in p])

      data["itemlist"].append(item)

    return data
