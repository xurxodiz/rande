from abc import ABC, abstractmethod
import requests

class RedditFeed(ABC):

  def __init__(self, subreddit):
    response = requests.get(f'https://www.reddit.com/r/{subreddit}.json')
    response.raise_for_status() # if any
    self.js = response.json()

  @abstractmethod
  def feed_data(self):
    pass
