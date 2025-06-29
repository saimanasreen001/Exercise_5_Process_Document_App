from queue import Queue
from threading import Thread
import time


class MessageBroker:
    def __init__(self):
        self.topics = {}

    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = Queue()

    def publish(self, topic_name, message):
        if topic_name in self.topics:
            self.topics[topic_name].put(message)

    def subscribe(self, topic_name, handler):
        def listen():
            while True:
                message = self.topics[topic_name].get()
                handler(message)

        Thread(target=listen, daemon=True).start()


broker = MessageBroker()
broker.create_topic("doc_uploaded")
