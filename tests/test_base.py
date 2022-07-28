import json
import os
import datetime
from typing import List
from configurations.Config import Config
from configurations.RabbitMqPublisherConfigure import RabbitMqPublisherConfigure
from models.Input import Input
from models.Output import Output
from proj_utils.Parser import Parser
from src.RabbitMqPublisher import RabbitMqPublisher
from tests.test_model.test_input import TestInput


class TestBase:
    PUBLISHER_CONFIGURE = RabbitMqPublisherConfigure(
        queue=Config.QUEUE,
        host=Config.HOST,
        routingKey=Config.ROUTING_KEY,
        exchange=Config.EXCHANGE
    )

    STUDENTS_DIR_PATH = "C:/Users/razm1/PycharmProjects/routeExerciseWTesting/students"

    @staticmethod
    def parse_output(input_model: TestInput) -> Output:
        return Parser(input_model.__dict__).parse_output()

    @staticmethod
    def read_from_file(filepath: str) -> json:

        TestBase.get_docs(1)

        with open(filepath, "r") as text_file:
            json_data = json.loads(text_file.read())

        return json_data

    @staticmethod
    def send_body(publisher: RabbitMqPublisher, body: TestInput):
        publisher.publish(str(json.dumps(body.__dict__)))

    @staticmethod
    def get_input_model(body):
        return Input(**json.loads(body))

    @staticmethod
    def get_docs(expected_docs: int, timeout_sec: int = 3000) -> List:
        date = datetime.datetime.now() + datetime.timedelta(milliseconds=timeout_sec)
        if expected_docs == 0:
            while date > datetime.datetime.now():
                if len(os.listdir(TestBase.STUDENTS_DIR_PATH)) != 0:
                    return os.listdir(TestBase.STUDENTS_DIR_PATH)
            return os.listdir(TestBase.STUDENTS_DIR_PATH)
        else:
            while len(os.listdir()) != expected_docs and date > datetime.datetime.now():
                result = os.listdir(TestBase.STUDENTS_DIR_PATH)
                if len(result) == expected_docs:
                    return result
            return os.listdir(TestBase.STUDENTS_DIR_PATH)