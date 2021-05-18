from graphene import ID, Field, List

from .models import Upload
from .node import Node
from .types import MeType, UploadType


class Queries(object):
    me = Field(MeType)
    upload = Field(UploadType, id=ID(required=True))
    uploads = Field(List(UploadType))

    def resolve_upload(self, info, id):
        return Upload.objects.get(id=Node.gid2id(id))

    def resolve_uploads(self, info):
        return Upload.objects.filter(user=info.context.user)

    def resolve_me(self, info):
        return info.context.user
