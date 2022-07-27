from configurations.Config import Config


class RabbitMqServerConfigure:
    def __init__(self, host=Config.HOST, queue=Config.QUEUE):
        self.host = host
        self.queue = queue
