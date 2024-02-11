from datetime import datetime
import html

from .reddit_feed import RedditFeed

class NintendoSwitch(RedditFeed):

  def __init__(self):
    super().__init__("NintendoSwitch")

  def feed_data(self):

    data = {
      "title": "Reddit - Nintendo Switch",
      "link": "https://reddit.com/r/NintendoSwitch/",
      "description": "The central hub for all news, updates, rumors, and topics relating to the Nintendo Switch. We are a fan-run community, not an official Nintendo forum.",
      "itemlist": []
    }

    for pt in self.js["data"]["children"]:

      post = pt["data"]
      item = {}

      item["pubDate"] = datetime.fromtimestamp(post['created'])

      item["title"] = post['title']
      item["link"] = f"https://reddit.com{post['permalink']}"

      if post["selftext_html"]:
        item["description"] = html.unescape(post['selftext_html'])

      if post["thumbnail"] != "self":
        item["media_thumbnail"] = post['thumbnail']

      data["itemlist"].append(item)

    return data
