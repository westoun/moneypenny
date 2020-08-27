#!/usr/bin/env python3

from androidhelper import sl4a
from time import sleep

from utils.logging.console_logger import ConsoleLogger


class AndroidAudioUtils():

    def __init__(self):
        self._logger = ConsoleLogger()

        self._droid = sl4a.Android()

    def speak(self, text):
        self._droid.ttsSpeak(text)

    def stop_listening(self):
        self._listening = False

    def listen(self, callback):
        self._listening = True
        self._run_listening_loop(callback)

    def _run_listening_loop(self, callback):

        while self._listening:
            if self._droid.ttsIsSpeaking()[1]:
                sleep(1)
                continue

            try:
                result = self._droid.recognizeSpeech()[1]
                callback(result)
                sleep(1)
            except Exception as e:
                self._logger.error(e)



