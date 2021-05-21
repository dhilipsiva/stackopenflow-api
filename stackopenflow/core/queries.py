from graphene import ID, Field, List
from graphene_django.debug import DjangoDebug

from .decorators import login_required
from .models import Upload
from .node import Node
from .types import UploadType, UserType


class Queries(object):
    debug = Field(DjangoDebug, name="_debug")
    me = Field(UserType)
    upload = Field(UploadType, id=ID(required=True))
    uploads = Field(List(UploadType))

    @login_required
    def resolve_upload(self, info, id):
        return Upload.objects.get(id=Node.gid2id(id))

    @login_required
    def resolve_uploads(self, info):
        return Upload.objects.filter(user=info.context.user)

    @login_required
    def resolve_me(self, info):
        return info.context.user
