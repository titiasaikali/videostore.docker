from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("create/", views.movie_create, name="movie_create"),
    path("<str:pk>/", views.movie_detail, name="movie_detail"),
    path("<str:pk>/edit/", views.movie_update, name="movie_update"),
    path("<str:pk>/delete/", views.movie_delete, name="movie_delete"),
]