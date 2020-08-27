#!/usr/bin/env python3

import wikipedia

from topics.topic import TopicAgent

NAME = "definition"
COMPARISON_COMMANDS = [
    "What is New York?",
    "Who is Sandro Boticelli?",
    "Define multithreading."
]


class DefinitionAgent(TopicAgent):

    def __init__(self, messenger):
        super(DefinitionAgent, self).__init__(
            messenger=messenger,
            name=NAME,
            comparison_commands=COMPARISON_COMMANDS)

        self._messenger.register_callback(self.process)

    def _extract_topic(self, command):
        # TODO: Use more elaborate nlp
        topic = command.split("what is")[-1]
        return topic

    def process(self, command):
        topic = self._extract_topic(command)
        # TODO: Learn 2 handle multiple topics.
        # wikipedia.set_lang('en')
        response = wikipedia.summary(topic, sentences=1)
        self.text_to_voice(response)

    def run(self):
        self._messenger.start_listening()

    def stop(self):
        self._messenger.stop_listening()
