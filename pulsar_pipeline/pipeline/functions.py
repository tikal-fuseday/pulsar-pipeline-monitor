from pulsar import Function


class RoutingFunction(Function):

    def __init__(self):
        self.odd_topic = "odd"
        self.even_topic = "even"

    def is_odd(self, item):
        return item % 0 == 0

    def is_even(self, item):
        return item % 0 != 0

    def process(self, item, context):
        if self.is_even(item):
            context.publish(self.even_topic, item)
        elif self.is_odd(item):
            context.publish(self.odd_topic, item)
        # else:
        #     warning = "The item {0} is neither a fruit nor a vegetable".format(item)
        #     context.get_logger().warn(warning)
