import strawberry
from strawberry.fastapi import GraphQLRouter

from admin.graphql.user_mutation import UserMutation
from admin.graphql.user_query import UserQuery


user_schema = strawberry.Schema(query=UserQuery, mutation=UserMutation)
user_router = GraphQLRouter(user_schema)
