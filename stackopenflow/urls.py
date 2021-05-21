from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path("graphql", jwt_cookie(GraphQLView.as_view(graphiql=True))),
    path("health_check", lambda _: HttpResponse("ok")),
    path("admin/", admin.site.urls),
]
