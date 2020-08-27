#!/usr/bin/env python3

from topics.topic import TopicAgent

NAME = "weather"
COMPARISON_COMMANDS = []


class WeatherAgent(TopicAgent):

    def __init__(self, messenger):
        super(WeatherAgent, self).__init__(
            messenger=messenger,
            name=NAME, 
            comparison_commands=COMPARISON_COMMANDS)

        self._messenger.register_callback(self.process)


    def process(self, command):
        # https://www.metaweather.com/api/#locationsearch
        response = 'I am not implemented yet!'
        self.text_to_voice(response)

    def run(self):
        self._messenger.start_listening()

    def stop(self):
        self._messenger.stop_listening()
