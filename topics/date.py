#!/usr/bin/env python3

from datetime import datetime, date

from topics.topic import TopicAgent

NAME = "date"
COMPARISON_COMMANDS = [
    "What is the date?",
    "Tell me the date.",
    "What date is it?"
]


class DateAgent(TopicAgent):
    def __init__(self, messenger):
        super(DateAgent, self).__init__(
            messenger=messenger,
            name=NAME, 
            comparison_commands=COMPARISON_COMMANDS)

        self._messenger.register_callback(self.process)

    def process(self, command):
        # TODO: Add more elaborate processing,
        # such as date next week.
        today = date.today()
        today = today.strftime("%B %d, %Y")
        response = f"Today, it is {today}"
        self.text_to_voice(response)

    def run(self):
        self._messenger.start_listening()

    def stop(self):
        self._messenger.stop_listening()
