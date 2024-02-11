from datetime import datetime
import html

from .reddit_feed import RedditFeed

class TrueGaming(RedditFeed):

  def __init__(self):
    super().__init__("truegaming")

  def feed_data(self):

    data = {
      "title": "Reddit - Nintendo Switch",
      "link": "https://reddit.com/r/truegaming/",
      "description": "For those who like talking about games as much as playing them. /r/truegaming is a subreddit dedicated to meaningful, insightful, and high-quality discussion on all topics gaming.",
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
