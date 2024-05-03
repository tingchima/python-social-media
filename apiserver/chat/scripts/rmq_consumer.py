from pprint import pprint

from pika import BlockingConnection, URLParameters

user_1 = 1
user_2 = 2


def on_message_callback(channel, method, properties, body):

    print(f"channel={channel}")

    pprint(f"body={body}")


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
    ch.exchange_declare(exchange="room_25", exchange_type="fanout", durable=True)

    # queue for room_25 from specified user(websocket client)
    queue_name_for_user_1 = "room_25_" + str(user_1)
    queue_for_user_1 = ch.queue_declare(
        queue=queue_name_for_user_1,  # queue name
        exclusive=True,  # kill queue when connection is closed
        arguments={"max-length-bytes": 1048576},  # 1mb length
    )
    queue_name_for_user_2 = "room_25_" + str(user_2)
    queue_for_user_2 = ch.queue_declare(
        queue=queue_name_for_user_2,
        exclusive=True,
        arguments={"max-length-bytes": 1048576},
    )

    # bind the queue with room_25 exchange
    ch.queue_bind(exchange="room_25", queue=queue_name_for_user_1)
    ch.queue_bind(exchange="room_25", queue=queue_name_for_user_2)

    ch.basic_consume(
        queue=queue_for_user_1.method.queue, on_message_callback=on_message_callback, auto_ack=True
    )
    ch.basic_consume(
        queue=queue_for_user_2.method.queue, on_message_callback=on_message_callback, auto_ack=True
    )

    ch.start_consuming()
