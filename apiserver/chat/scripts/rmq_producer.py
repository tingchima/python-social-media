from dataclasses import dataclass

from pika import BasicProperties, BlockingConnection, URLParameters

user_1 = 1
user_2 = 2


@dataclass
class Foomessage:
    uuid: str
    user_id: int
    content: str


def run():
    rabbitmq_url = "{}://{}:{}@{}:{}{}".format(
        "amqp",
        "guest",
        "guest",
        "localhost",
        5672,
        "/",
    )
    rabbitmq_connection = BlockingConnection(parameters=URLParameters(rabbitmq_url))

    ch = rabbitmq_connection.channel()

    # # fanout type of exchange
    ch.exchange_declare(exchange="room_1", exchange_type="fanout", durable=True)
    # ch.queue_declare(queue="room_1_1") # use routing key
    ch.basic_publish(
        exchange="room_1",
        # exchange="",
        routing_key="room_1_1",
        # body=Foomessage(uuid=uuid4(), user_id=3, content="test rmq message..."),
        body="test rmq message..",
        properties=BasicProperties(delivery_mode=2),
    )

    print("PUBLISH.....")

    rabbitmq_connection.close()
