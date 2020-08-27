#!/usr/bin/env python3

from datetime import datetime, date

from topics.topic import TopicAgent

NAME = "default"
COMPARISON_COMMANDS = []


class DefaultAgent(TopicAgent):

    def __init__(self, messenger):
        super(DefaultAgent, self).__init__(
            messenger=messenger,
            name=NAME, 
            comparison_commands=COMPARISON_COMMANDS)

        self._messenger.register_callback(self.process)

    def process(self, command):
        # TODO: Randomly select from multiple phrases.
        response = "I did not get that. Please repeat!"
        self.text_to_voice(response)

    def run(self):
        self._messenger.start_listening()

    def stop(self):
        self._messenger.stop_listening()
