#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/30/22, 9:19 PM"
#

from django.urls import path

from apps.cic_cms.views.dashboard import DashboardView

app_name = "cms"
urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
]
