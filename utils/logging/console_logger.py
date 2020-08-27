#!/usr/bin/env python3

from utils.logging.logger import Logger

class ConsoleLogger(Logger):

    def debug(self, message):
        print(f"DEBUG: {message}")

    def info(self, message):
        print(f"INFO: {message}")

    def warning(self, message):
        print(f"WARNING: {message}")

    def error(self, message):
        print(f"ERROR: {message}")