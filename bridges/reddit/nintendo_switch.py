from .reddit_feed import RedditFeed

class NintendoSwitch(RedditFeed):

  def __init__(self):
    data = {
      "title": "Reddit - Nintendo Switch",
      "link": "https://reddit.com/r/NintendoSwitch/",
      "description": "The central hub for all news, updates, rumors, and topics relating to the Nintendo Switch. We are a fan-run community, not an official Nintendo forum.",
      "itemlist": []
    }
    super().__init__("NintendoSwitch", data)

