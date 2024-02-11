from datetime import datetime
import html
import requests

class RedditFeed():

  def __init__(self, subreddit, data):
    response = requests.get(f'https://www.reddit.com/r/{subreddit}.json')
    response.raise_for_status() # if any
    self.js = response.json()
    self.data = data

  def feed_data(self):

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

      self.data["itemlist"].append(item)

    return self.data

