class Producer:

    def __init__(self, client, name):
        self.name = f'main{name}'
        self.producer = client.create_producer(f'main{name}')

    def send_msg(self):
        for i in range(10):
            self.producer.send(('Hello-%d' % i).encode('utf-8'))
