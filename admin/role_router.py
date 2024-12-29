import strawberry
from strawberry.fastapi import GraphQLRouter

from admin.role_query import RoleQuery


role_schema = strawberry.Schema(query=RoleQuery, mutation=None)
role_router = GraphQLRouter(role_schema)
