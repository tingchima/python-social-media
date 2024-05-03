from pprint import pprint
from uuid import uuid4

from chat.domain.entities import RoomType
from chat.infrastructure.potgres.chatroom_repository import ChatroomRepository
from chat.models import Chatroom, ChatroomMember
from django.core.paginator import Paginator
from django.db import connection


def run():
    try:
        # # save
        # model = Chatroom(
        #     room_name=f"room_{uuid4()}",
        #     room_type="GROUP",
        #     avatar_url="",
        # )
        # model.save()
        # print(f"id={model.id}")

        # all
        limit = 10
        offset = 1

        # query_builder = Chatroom.objects.filter(room_type=RoomType.GROUP.name)
        # total_size = query_builder.count()
        # print(f"total_size={total_size}")

        # offset = (offset - 1) * limit
        # limit = offset + limit

        # models = query_builder.order_by("created_at").reverse()[offset:limit]
        # print(f"count={len(models)}")
        # print([model.created_at for model in models])

        # pprint(connection.queries)

        models = (
            Chatroom.objects.filter(room__user_id=1)
            .prefetch_related("room")
            .order_by("-last_message_timestamp", "-created_at")
            # [offset:limit]
        )
        pprint(f"total={len(models)}")
        # pprint([model for model in models])

        paginator = Paginator(models, limit)
        page_mdoels = paginator.page(offset)
        pprint(f"page_total={len(page_mdoels)}")
        pprint(connection.queries)

    except Exception as e:
        print(f"orm_error={e}")
    # print(entity)

    # get_by_id
    # room = ChatroomRepository().get_by_id(id=2)
    # print(room)

    # delete_by_id
    # ChatroomRepository().delete_by_key(id=2)
