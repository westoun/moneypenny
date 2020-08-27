#!/usr/bin/env python3

import numpy as np
import speech_recognition as sr
from subprocess import call
from time import sleep

from topics.date import DateAgent
from topics.time import TimeAgent
from topics.definition import DefinitionAgent
from topics.default import DefaultAgent
from topics.music import MusicAgent
from topics.news import NewsAgent
from utils.audio.audio_utils_factory import AudioUtilsFactory
from utils.ipc.messenger import QueueMessenger
from utils.logging.console_logger import ConsoleLogger
from utils.similarity.similarity_utils_factory import SimilarityUtilsFactory


TOPIC_AGENTS = [
    DateAgent,
    TimeAgent,
    DefinitionAgent,
    MusicAgent,
    NewsAgent
]

DEFAULT_AGENT = DefaultAgent


class MoneyPenny():

    def __init__(self, platform="osx"):
        self._logger = ConsoleLogger()

        self._similarity_utils = SimilarityUtilsFactory().get_similarity_utils()

        self._audio_utils = AudioUtilsFactory(
            platform=platform).get_audio_utils()

        self._topic_agents = []
        self._default_agent = None
        self._messenger_dict = {}

        self._init_agents()

    def _init_agents(self):
        self._init_topic_agents()
        self._init_default_agent()

    def _init_topic_agents(self):
        for AgentClass in TOPIC_AGENTS:
            messenger = QueueMessenger()
            agent = AgentClass(messenger)
            self._topic_agents.append(agent)
            self._messenger_dict[agent.name] = messenger

    def _init_default_agent(self):
        messenger = QueueMessenger()
        agent = DEFAULT_AGENT(messenger)
        self._default_agent = agent
        self._messenger_dict[agent.name] = messenger

    def _listen(self, command):
        self._logger.info(f"Understood '{command}'")

        valid = self._evaluate_command(command)
        if not valid:
            return

        command = self._preprocess_command(command)

        agent = self._get_most_probable_agent(command, threshold=0.5)
        self._send_command_to_agent(agent, command)

    def _evaluate_command(self, command):
        command = command.lower()

        if 'moneypenny' in command or 'money penny' in command:
            return True
        else:
            self._logger.warning('The command has to include "moneypenny"!')
            return False

    def _preprocess_command(self, command):
        command = command.lower()

        if 'moneypenny' in command:
            command = command.split("moneypenny")[-1]
        elif 'money penny' in command:
            command = command.split("money penny")[-1]

        return command

    def _get_most_probable_agent(self, command, threshold=0):
        highest_similarities = []
        for agent in self._topic_agents:
            highest_similarity = 0
            for comparison_command in agent.comparison_commands:
                similarity = self._similarity_utils.get_similarity(
                    command, comparison_command)
                if similarity > highest_similarity:
                    highest_similarity = similarity
            highest_similarities.append(highest_similarity)

        if len([similarity for similarity in highest_similarities if similarity > threshold]) > 0:
            agent_index = np.argmax(highest_similarities)
            return self._topic_agents[agent_index]
        else:
            return self._default_agent

    def _send_command_to_agent(self, agent, command):
        messenger = self._messenger_dict[agent.name]
        messenger.send(command)

    def start(self):
        self._audio_utils.listen(self._listen)

        self._audio_utils.speak("I am ready to listen to you.")

        self._default_agent.start()
        for agent in self._topic_agents:
            agent.start()

    def stop(self):
        self._audio_utils.stop_listening()

        self._default_agent.stop()
        for agent in self._topic_agents:
            agent.stop()

        self._logger.info('stopped moneypenny')


if __name__ == "__main__":
    mp = MoneyPenny()

    try:
        mp.start()
    except KeyboardInterrupt:
        mp.stop()
