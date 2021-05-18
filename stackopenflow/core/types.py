from graphene.types import ID, JSONString, ObjectType, String
from graphene_django import DjangoObjectType

from .models import Upload
from .node import Node
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
        interfaces = (Node,)
        convert_choices_to_enum = False

    def resolve_presigned_post_url(self, info):
        return generate_presigned_post(self.key)
