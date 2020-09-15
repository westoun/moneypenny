#!/usr/bin/env python3

from bs4 import BeautifulSoup
import pafy
from time import sleep
from threading import Thread
from urllib.parse import *
import urllib.request
import vlc

from topics.topic import TopicAgent
from utils.logging.console_logger import ConsoleLogger

NAME = "music"
COMPARISON_COMMANDS = [
    "Play bad touch from blodhound gang.",
    "Play nothing else matters.",
    "Play the piano man by billy joel.",
    "Stop playing music.",
    "Raise the volume.",
    "Lower the volume.",
    "Stop music.",
    "Resume music."
]


class MusicAgent(TopicAgent):

    def __init__(self, messenger):
        super(MusicAgent, self).__init__(
            messenger=messenger,
            name=NAME, 
            comparison_commands=COMPARISON_COMMANDS)

        self._logger = ConsoleLogger()
        self._player = None

        self._messenger.register_callback(self.process)

    def _get_url(self, title):
        # based on https://github.com/dashvinsingh/YoutubeAudio-Python-Stream/blob/master/youtube_stream.py
        query = urllib.parse.quote(title)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        sleep(1)
        html = response.read()

        try:
            soup = BeautifulSoup(html, 'lxml')
            video_urls = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
            video_url = 'https://www.youtube.com' + video_urls[0]['href']
        except IndexError:
            return self._get_url(title)

        video = pafy.new(video_url)
        best = video.getbestaudio()
        playurl = best.url
        return playurl

    def _play_audio_from_url(self, url):
        Instance = vlc.Instance()
        self._player = Instance.media_player_new()
        Media = Instance.media_new(url)
        Media.get_mrl()
        self._player.set_media(Media)
        self._player.play()
        while self._player and not self._player.is_playing():
            sleep(0.2)
        while self._player is not None and self._player.is_playing():
            sleep(1)

    def _play_audio(self, title):
        self._logger.info('play entered')
        if self._player and self._player.is_playing():
            self._stop_audio()

        url = self._get_url(title)

        playing_thread = Thread(target=self._play_audio_from_url, args=[url])
        playing_thread.start()

    def _pause_audio(self):
        print('pause entered')
        if self._player is not None:
            self._player.pause()

    def _stop_audio(self):
        self._logger.info('stop entered')
        if self._player is not None:
            self._player.stop()
            self._player = None

    def _resume_audio(self):
        self._logger.info('resume entered')
        if self._player is not None:
            self._player.pause()

    def _raise_volume(self):
        self._logger.info('raise volume entered')
        if self._player is not None:
            volume = self._player.audio_get_volume()
            raised_volume = max(volume + 10, 100)
            self._player.audio_set_volume(raised_volume)

    def _lower_volume(self):
        self._logger.info('lower volume entered')
        if self._player is not None:
            volume = self._player.audio_get_volume()
            raised_volume = min(volume - 10, 0)
            self._player.audio_set_volume(raised_volume)

    def process(self, command):
        if 'play' in command:
            # TODO: Use more elaborate nlp
            title = command.split("play")[-1]
            self._play_audio(title)
        elif 'pause' in command:
            self._pause_audio()
        elif 'resume' in command:
            self._resume_audio()
        elif 'stop' in command:
            self._stop_audio()
        elif 'raise' in command:
            self._raise_volume()
        elif 'lower' in command:
            self._raise_volume()

        return ''

    def run(self):
        self._messenger.start_listening()

    def stop(self):
        self._messenger.stop_listening()


# ma = MusicAgent()
# ma.process('play bad touch')
# sleep(5)
# ma.process('pause music')
# sleep(5)
# ma.process('resume music')
# sleep(5)
# ma.process('louder!!!')
# sleep(5)
# ma.process('stop music playback.')
# sleep(3)
# ma.process('play californication by rhcp')
