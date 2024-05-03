import boto3
from chat.application.chatroom_service import ChatroomService
from chat.application.message_service import MessageService
from config.django.base import (
    AWS_DYNAMODB_LOCAL,
    RABBITMQ_HOST,
    RABBITMQ_PASSWORD,
    RABBITMQ_PORT,
    RABBITMQ_SCHEME,
    RABBITMQ_USERNAME,
    RABBITMQ_VIRTUAL_HOST,
)
from pika import BlockingConnection, URLParameters

chatroom_service: ChatroomService = ChatroomService()

dynamodb = boto3.resource(
    service_name="dynamodb",
    endpoint_url=AWS_DYNAMODB_LOCAL,
)

rabbitmq_url = "{}://{}:{}@{}:{}{}".format(
    RABBITMQ_SCHEME,
    RABBITMQ_USERNAME,
    RABBITMQ_PASSWORD,
    RABBITMQ_HOST,
    RABBITMQ_PORT,
    RABBITMQ_VIRTUAL_HOST,
)
rabbitmq = BlockingConnection(parameters=URLParameters(rabbitmq_url))


message_service: MessageService = MessageService(
    chatroom_service=chatroom_service, dynamodb=dynamodb, rabbitmq=rabbitmq
)
