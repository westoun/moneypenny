#!/usr/bin/env python3

from datetime import datetime, date

from topics.topic import TopicAgent

NAME = "time"
COMPARISON_COMMANDS = [
    "What time is it?",
    "What is the time?",
    "Tell me the time."
]


class TimeAgent(TopicAgent):

    def __init__(self, messenger):
        super(TimeAgent, self).__init__(
            messenger=messenger,
            name=NAME, 
            comparison_commands=COMPARISON_COMMANDS)

        self._messenger.register_callback(self.process)

    def process(self, command):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        response = f"Right now, it is {time}"
        self.text_to_voice(response)

    def run(self):
        self._messenger.start_listening()

    def stop(self):
        self._messenger.stop_listening()
