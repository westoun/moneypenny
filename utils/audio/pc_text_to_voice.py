#!/usr/bin/env python3

# Note: This file became necessary as a workaround
# since pyttsx3 is not thread-safe.
# See https://github.com/nateshmbhat/pyttsx3/issues/8
# for further details.

import pyttsx3
# id: 3 is french, 4 is german, 10 & 28 is english
import sys


def init_engine(language_code):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[language_code].id)
    return engine


def say(s):
    engine.say(s)
    engine.runAndWait()  # blocks


text = str(sys.argv[1])

try:
    language = str(sys.argv[2])
except:
    language = "en"

if language == "de":
    language_code = 4
elif language == "fr":
    language_code = 3
else:
    language_code = 10

engine = init_engine(language_code)
say(text)
