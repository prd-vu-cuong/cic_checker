from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.cic_core.routers")),
    path("admin/", admin.site.urls),
]
