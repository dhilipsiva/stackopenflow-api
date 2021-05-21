from graphene import ObjectType, Schema

from stackopenflow.core.mutations import Mutations as CoreMutations
from stackopenflow.core.queries import Queries as CoreQueries
from stackopenflow.qna.mutations import Mutations as QNAMutations
from stackopenflow.qna.queries import Queries as QNAQueries


class Query(
    CoreQueries,
    QNAQueries,
    # lastly,
    ObjectType,
):
    pass


class Mutation(
    CoreMutations,
    QNAMutations,
    # lastly,
    ObjectType,
):
    pass


schema = Schema(query=Query, mutation=Mutation)
