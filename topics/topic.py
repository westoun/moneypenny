#!/usr/bin/env python3

from subprocess import call
from threading import Event
from threading import Thread

from utils.audio.audio_utils_factory import AudioUtilsFactory

DEFAULT_NAME = ""
DEFAULT_COMPARISON_COMMANDS = []

class TopicAgent:

    def __init__(self, messenger, name=DEFAULT_NAME, comparison_commands=DEFAULT_COMPARISON_COMMANDS):

        self._messenger = messenger
        self._name = name 
        self._comparison_commands = comparison_commands

        self._audio_utils = AudioUtilsFactory().get_audio_utils()

    def process(self, command):
        raise NotImplementedError('You need to implement the process function!')

    def run(self):
        raise NotImplementedError('You need to implement the run function!')

    def stop(self):
        raise NotImplementedError('You need to implement the stop function!')

    def text_to_voice(self, text, language="en"):
        self._audio_utils.speak(text, language)

    @property 
    def name(self):
        return self._name

    @property
    def comparison_commands(self):
        return self._comparison_commands

    def start(self):
        thread = Thread(target=self.run, args=())
        thread.start()

        # TODO: Implement stop event that is passed as args
