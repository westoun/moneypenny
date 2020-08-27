#!/usr/bin/env python3

class Logger:

    def debug(self, message):
        raise NotImplementedError()

    def info(self, message):
        raise NotImplementedError()

    def warning(self, message):
        raise NotImplementedError()

    def error(self, message):
        raise NotImplementedError