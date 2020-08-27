#!/usr/bin/env python3

from functools import partial
import speech_recognition as sr
from subprocess import call

from utils.logging.console_logger import ConsoleLogger

class PcAudioUtils():

    def __init__(self):
        self._logger = ConsoleLogger()

        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()

        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source)

    def speak(self, text, language="en"):
        if text is not None:
            call(['python3', 'utils/audio/pc_text_to_voice.py', text, language])

    def stop_listening(self):
        raise NotImplementedError("listen has to be called first!")

    def listen(self, callback):
        listener_callback = partial(
            self._listen_for_command, callback)

        stop_recognizer = self._recognizer.listen_in_background(
            self._microphone, listener_callback)

        self.stop_listening = stop_recognizer

    def _listen_for_command(self, callback, _, audio):
        try:

            command = self._recognizer.recognize_google(audio)
            callback(command)

        except sr.UnknownValueError:
            self._logger.warning("A Value error occurred. Please repeat!")
        except sr.RequestError as e:
            self._logger.error(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
