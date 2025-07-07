#asyncio is a python library used to write asynchronous code.
import asyncio

#MessageBroker class will manage:
    # 1.Topic
    # 2.Publish mssgs to topic.
    # 3.Listening/subscribing to mssg/topics.
class MessageBroker:

    #Initializes an empty dictionary to hold topic queues.
    def __init__(self):
        self.topics = {}

    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = asyncio.Queue()

    #publish does not automatically process the mssg rather stores it in the queue.
    async def publish(self, topic_name, message):
        if topic_name in self.topics:
            await self.topics[topic_name].put(message)

    def subscribe(self, topic_name, handler):
        async def listen():
            #if there is a mssg on the topic, handler is called.
            while True:
                message = await self.topics[topic_name].get()
                await handler(message)

        asyncio.create_task(listen())


broker = MessageBroker()
broker.create_topic("doc_uploaded")
