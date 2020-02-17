from time import sleep

import pulsar

from pipeline.producer import Producer
from pipeline.subscriber import Subscriber


if __name__ == "__main__":
    client = pulsar.Client('pulsar://localhost:6650')
    producer = Producer(client, 1).send_msg()
    subs = []
    for i in range(2, 6):
        producer = Producer(client, i)
        subs.append(Subscriber(client, i-1, producer))
    for sub in subs:
        sub.start_subscribing()
    client.close()
