#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuong"
#  __date_time = "7/24/22, 5:33 PM"


from django.urls import path, include
from rest_framework import routers
from .views import SingleCheckViewSet, MultiCheckViewSet

router = routers.DefaultRouter()
router.register(r"single", SingleCheckViewSet, basename="single-check")
router.register(r"multi", MultiCheckViewSet, basename="multi-check")

urlpatterns = [
    path("", include(router.urls)),
]
