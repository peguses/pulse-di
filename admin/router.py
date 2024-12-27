import strawberry
from strawberry.fastapi import GraphQLRouter

from admin.mutation import Mutation
from admin.query import Query


schema = strawberry.Schema(query=Query, mutation=Mutation)
user_router = GraphQLRouter(schema)
