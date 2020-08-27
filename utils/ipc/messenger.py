#!/usr/bin/env python3

from multiprocessing import Queue

class QueueMessenger():

    def __init__(self):
        self._queue = Queue(1) 
        self._callbacks = []
        self._listen = True

    def register_callback(self, callback):
        self._callbacks.append(callback)

    def start_listening(self):
        while self._listen:
            item = self._queue.get(block=True)

            for callback in self._callbacks:
                callback(item) 

    def stop_listening(self):
        self._listen = False

    def send(self, item):
        self._queue.put(item, block=True)