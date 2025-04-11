from . import views
from django.urls import path, include

app_name = 'homepage'

urlpatterns = [
    path("", views.index, name="index"),

    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]