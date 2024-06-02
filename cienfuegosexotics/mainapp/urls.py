from django.urls import path

from . import views

app_name = "mainapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("peppers/", views.peppers, name="peppers"),
    path("learning/", views.learning, name="learning"),
    path("mantises/", views.mantises, name="mantises"),
    path("tomatoes/", views.tomatoes, name="tomatoes"),
    path("contact/", views.contact, name="contact"),
]
