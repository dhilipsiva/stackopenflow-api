from graphene import ID, Field, List

from stackopenflow.core.decorators import login_required
from stackopenflow.core.node import Node

from .models import Question
from .types import QuestionType


class Queries(object):
    question = Field(QuestionType, id=ID(required=True))
    questions = Field(List(QuestionType))

    @login_required
    def resolve_question(self, info, id):
        return Question.objects.with_vote_count().get(id=Node.gid2id(id))

    @login_required
    def resolve_questions(self, info):
        return Question.objects.with_comment_count().with_vote_count()
