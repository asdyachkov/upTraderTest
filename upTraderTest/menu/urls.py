from django.urls import path
from . import views

urlpatterns = [
    path("menu/<str:title>/", views.index, name="menu"),
    path("menu/", views.index, name="menu_empty"),
]
