from pprint import pprint

from pika import BlockingConnection, URLParameters


def _on_message_callback(channel, method, properties, body):
    pass


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

    for i in range(100):
        idx = i + 1
        print(f"current={idx}")
        channel = rabbitmq_connection.channel()

        exchange = "room_{}".format(str(idx))
        channel.exchange_declare(exchange=exchange, exchange_type="fanout", durable=True)
        queue_name = "{}_user_{}".format(exchange, str(idx))
        queue = channel.queue_declare(
            queue=queue_name,  # queue name
            exclusive=True,  # kill queue when connection is closed
            arguments={"max-length-bytes": 1048576},  # 1mb length
        )
        print("BINDINGGGGGGGGG before")
        channel.queue_bind(exchange=exchange, queue=queue_name)

        print("BINDINGGGGGGGGG after")

        # send system message
        # message = f"welcome to chatroom {self.room_id}"
        # datetime_str = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        # self.send(text_data=json.dumps({"message": f"{datetime_str}:{message}"}))
        # start consuming rabbitmq fanout message from apiserver
        channel.basic_consume(
            queue=queue.method.queue,
            auto_ack=True,
            on_message_callback=_on_message_callback,
        )
