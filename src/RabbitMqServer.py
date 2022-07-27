import json
import pika

from configurations.Config import Config
from configurations.RabbitMqServerConfigure import RabbitMqServerConfigure
from proj_utils.Parser import Parser


class RabbitMqServer:
    def __init__(self, server: RabbitMqServerConfigure):
        self.server = server
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)
        print("Server started...")
        print("[X] Waiting for data...")

    @staticmethod
    def callback(ch, method, properties, body):
        string_body = body.decode('utf-8')

        try:
            RabbitMqServer.parse_to_text_file(string_body)
        except Exception as ex:
            print(ex)

    @staticmethod
    def parse_to_text_file(string_body):
        json_body = json.loads(string_body)
        parser = Parser(json_body)
        print(f"[X] Data Received for: {parser.parse_output().studentDetails.fullName}")
        parser.create_text_file()
        print("[X] Done !")

    def start_server(self):
        self._channel.basic_consume(
            queue=self.server.queue,
            on_message_callback=RabbitMqServer.callback,
            auto_ack=True
        )
        self._channel.start_consuming()


if __name__ == "__main__":
    server_configure = RabbitMqServerConfigure(host=Config.HOST, queue=Config.QUEUE)
    rabbitmq_server = RabbitMqServer(server=server_configure)
    rabbitmq_server.start_server()