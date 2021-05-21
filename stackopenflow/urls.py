from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

from stackopenflow.core.views import health_check

urlpatterns = [
    path(r"graphql", jwt_cookie(GraphQLView.as_view(graphiql=True))),
    path("health_check", health_check),
    path("admin/", admin.site.urls),
]
