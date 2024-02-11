from abc import ABC, abstractmethod
from lxml import etree
import requests

class HtmlFeed(ABC):

  def __init__(self, url):
    response = requests.get(url)
    parser = etree.HTMLParser()
    self.root = etree.fromstring(response.text, parser)

  @abstractmethod
  def feed_data(self):
    pass
