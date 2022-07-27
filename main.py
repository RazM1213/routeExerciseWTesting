from configurations.Config import Config
from configurations.RabbitMqServerConfigure import RabbitMqServerConfigure
from src.RabbitMqServer import RabbitMqServer


def main():
    server_configure = RabbitMqServerConfigure(host=Config.HOST, queue=Config.QUEUE)
    rabbitmq_server = RabbitMqServer(server=server_configure)
    rabbitmq_server.start_server()


if __name__ == "__main__":
    main()

