#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuong"
#  __date_time = "7/24/22, 10:02 AM"

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="cic_auth/login.html"),
        name="login",
    ),
    path("", include("django.contrib.auth.urls")),
]
