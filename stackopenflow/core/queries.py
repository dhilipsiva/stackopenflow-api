from django.conf import settings
from django.urls import reverse
from graphene import ID, Field, List

from .models import Upload
from .node import CustomNode
from .types import MeType, SocialBeginUrlType, UploadType


class Queries(object):
    me = Field(MeType)
    upload = Field(UploadType, id=ID(required=True))
    uploads = Field(List(UploadType))
    social_begin_urls = Field(List(SocialBeginUrlType))

    def resolve_upload(self, info, id):
        return Upload.objects.get(id=CustomNode.gid2id(id))

    def resolve_uploads(self, info):
        return Upload.objects.filter(user=info.context.user)

    def resolve_me(self, info):
        return info.context.user

    def resolve_social_begin_urls(self, info):
        urls = []
        for provider in settings.SOCIAL_PROVIDERS:
            path = reverse("social:begin", kwargs={"backend": provider})
            urls.append({"path": path, "provider": provider})
        return urls
