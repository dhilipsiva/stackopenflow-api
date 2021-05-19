from django.contrib import admin
from django.urls import include, path
from graphene_django.views import GraphQLView

urlpatterns = [
    path(r"graphql", GraphQLView.as_view(graphiql=True)),
    path("", include("social_django.urls", namespace="social")),
    path("admin/", admin.site.urls),
]
