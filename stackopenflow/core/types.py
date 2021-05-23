from django.contrib.contenttypes.models import ContentType
from graphene.types import JSONString
from graphene_django import DjangoObjectType

from .models import Upload, User
from .node import Node
from .storage import generate_presigned_post


class UserType(DjangoObjectType):
    class Meta:
        model = User


class UploadType(DjangoObjectType):

    presigned_post_url = JSONString()

    class Meta:
        model = Upload
        interfaces = (Node,)
        convert_choices_to_enum = False

    def resolve_presigned_post_url(self, info):
        return generate_presigned_post(self.key)


class ContentTypeType(DjangoObjectType):
    class Meta:
        model = ContentType
