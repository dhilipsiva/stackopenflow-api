from celery import current_app
from graphene import Field
from graphene.relay import ClientIDMutation

from .choices import UploadStatus
from .inputs import CreateUploadInput, IDInput, UpdateMeInput
from .models import Upload, User
from .node import Node
from .types import MeType, UploadType


class CreateUpload(ClientIDMutation):
    Input = CreateUploadInput
    upload = Field(UploadType)

    @staticmethod
    def mutate_and_get_payload(root, info, **input):
        upload = Upload.objects.create(user=info.context.user, **input)
        return CreateUpload(upload=upload)


class FinishUpload(ClientIDMutation):
    Input = IDInput
    upload = Field(UploadType)

    @staticmethod
    def mutate_and_get_payload(root, info, **input):
        upload = Upload.objects.get(id=Node.gid2id(input.get("id")))
        upload.status = UploadStatus.UPLOADED
        upload.save()
        current_app.send_task("stackopenflow.core.tasks.process_upload", (upload.id,))
        return FinishUpload(upload=upload)


class UpdateMe(ClientIDMutation):
    Input = UpdateMeInput
    me = Field(MeType)

    @staticmethod
    def mutate_and_get_payload(root, info, **input):
        User.objects.filter(id=info.context.user.id).update(**input)
        me = User.objects.get(id=info.context.user.id)
        return UpdateMe(me=me)


class Mutations:
    create_upload = CreateUpload.Field()
    node = Node.Field()
    update_me = UpdateMe.Field()
    finish_upload = FinishUpload.Field()
