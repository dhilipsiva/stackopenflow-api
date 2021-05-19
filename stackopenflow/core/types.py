from graphene.types import ID, JSONString, ObjectType, String
from graphene_django import DjangoObjectType

from .models import Upload
from .node import CustomNode
from .storage import generate_presigned_post


class UserType(ObjectType):
    id = ID()


class MeType(ObjectType):
    email = String()
    id = ID()


class UploadType(DjangoObjectType):

    presigned_post_url = JSONString()

    class Meta:
        model = Upload
        interfaces = (CustomNode,)
        convert_choices_to_enum = False

    def resolve_presigned_post_url(self, info):
        return generate_presigned_post(self.key)


class SocialBeginUrlType(ObjectType):
    path = String()
    provider = String()
