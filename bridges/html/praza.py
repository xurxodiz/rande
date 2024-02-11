from lxml import etree

from .html_feed import HtmlFeed

class Praza(HtmlFeed):

  def __init__(self):
    super().__init__('https://praza.gal/')

  def feed_data(self):
    data = {
      "title": "Praza Pública",
      "link": "https://praza.gal/",
      "description": "O xornal da Galicia que vén.",
      "itemlist": []
    }

    for article in self.root.iterfind(".//article"):

      item = {}

      if (dt := article.find(".//time[@datetime]")) is not None:
        item["pubDate"] = dt.get('datetime')

      if (header := article.find(".//h2")) is not None:
          if (a := header.find(".//a")) is not None:
            item["title"] = a.text
            item["link"] = f"https://praza.gal{a.get('href')}"

      if (p := article.find(".//p")) is not None:
          item["description"] = ''.join([p.text or ''] + [etree.tostring(e, encoding='unicode') for e in p])

      if (img := article.find(".//img[@class='article-summary-image']")) is not None:
        item["media_thumbnail"] = img.get('src')

      data["itemlist"].append(item)

    return data
