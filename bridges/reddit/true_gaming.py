from .reddit_feed import RedditFeed

class TrueGaming(RedditFeed):

  def __init__(self):
    data = {
      "title": "Reddit - Nintendo Switch",
      "link": "https://reddit.com/r/truegaming/",
      "description": "For those who like talking about games as much as playing them. /r/truegaming is a subreddit dedicated to meaningful, insightful, and high-quality discussion on all topics gaming.",
      "itemlist": []
    }
    super().__init__("truegaming", data)
