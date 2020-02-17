from pipeline.producer import Producer


class Subscriber:

    def __init__(self, client, name, producer):
        self.name = f'subscribe{name}'
        self.consumer = client.subscribe(f'main{name}', self.name)
        self.producer = producer

    def start_subscribing(self):
        for i in range(10):
            msg = self.consumer.receive()
            try:
                print(f"{self.name}: Received message '{msg.data()}' id='{msg.message_id()} producer={self.producer.name}'")
                # Acknowledge successful processing of the message
                self.consumer.acknowledge(msg)
            except:
                # Message failed to be processed
                self.consumer.negative_acknowledge(msg)
        self.producer.send_msg()
