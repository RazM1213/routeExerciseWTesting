from configurations.Config import Config


class RabbitMqPublisherConfigure:

    def __init__(self, queue=Config.QUEUE, host=Config.HOST, routingKey=Config.ROUTING_KEY, exchange=Config.EXCHANGE):
        self.queue = queue
        self.host = host
        self.routingKey = routingKey
        self.exchange = exchange
