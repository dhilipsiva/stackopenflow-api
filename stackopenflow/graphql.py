from graphene import ObjectType, Schema

from stackopenflow.core.mutations import Mutations as CoreMutations
from stackopenflow.core.queries import Queries as CoreQueries


class Query(
    CoreQueries,
    # lastly,
    ObjectType,
):
    pass


class Mutation(
    CoreMutations,
    # lastly,
    ObjectType,
):
    pass


schema = Schema(query=Query, mutation=Mutation)
