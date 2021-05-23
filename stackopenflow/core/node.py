from django.conf import settings
from graphene.relay import Node as _Node


class Node(_Node):
    @staticmethod
    def gid2id(gid):
        return Node.from_global_id(gid)[1]

    @staticmethod
    def from_global_id(gid):
        return gid.split(settings.NODE_DIVIDER, 1)

    @staticmethod
    def to_global_id(type, id):
        return f"{type}{settings.NODE_DIVIDER}{id}"
