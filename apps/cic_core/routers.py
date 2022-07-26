from django.urls import path, include


urlpatterns = [
    path("", include("apps.cic_single.urls")),
    path("auth/", include("apps.cic_auth.urls")),
    path("api/", include("apps.cic_api.urls")),
]
