import strawberry
from strawberry.fastapi import GraphQLRouter

from admin.graphql.role_query import RoleQuery
from admin.graphql.user_mutation import UserMutation
from admin.graphql.user_query import UserQuery


@strawberry.type
class Query(RoleQuery, UserQuery):
    pass


@strawberry.type
class Mutation(UserMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_router = GraphQLRouter(schema)
