from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home, name="cms"),
    path("import_data/", views.import_data, name="import_data"),
    path("customer/", views.customer),
]
