#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

from topics.topic import TopicAgent

RSS_URL = "https://www.tagesschau.de/xml/rss2_https/"

NAME = "news"
COMPARISON_COMMANDS = [
    "What's the news?",
    "What's new?"
]


class NewsAgent(TopicAgent):

    def __init__(self, messenger):
        super(NewsAgent, self).__init__(
            messenger=messenger,
            name=NAME,
            comparison_commands=COMPARISON_COMMANDS)

        self._messenger.register_callback(self.process)

    def process(self, command):
        xml = self._fetch_xml(RSS_URL)
        news = self._extract_news(xml)

        for title in news:
            self.text_to_voice(title, language="de")

    def _fetch_xml(self, url):
        response = requests.get(url)
        xml = response.content
        return xml

    def _extract_news(self, xml):
        soup = BeautifulSoup(xml, "xml")
        items = soup.find_all("item")

        news = []
        for item in items:
            news.append(item.title.text)

        return news[:10]

    def run(self):
        self._messenger.start_listening()

    def stop(self):
        self._messenger.stop_listening()

