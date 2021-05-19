from django.conf import settings
from graphene.relay import Node


class CustomNode(Node):
    @staticmethod
    def gid2id(gid):
        return CustomNode.from_global_id(gid)[1]

    @staticmethod
    def from_global_id(gid):
        return gid.split(settings.DIVIDER, 1)

    @staticmethod
    def to_global_id(type, id):
        return f"{type}{settings.DIVIDER}{id}"
