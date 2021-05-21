from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    path(r"graphql", jwt_cookie(GraphQLView.as_view(graphiql=True))),
    path("", include("social_django.urls", namespace="social")),
    path("admin/", admin.site.urls),
]
