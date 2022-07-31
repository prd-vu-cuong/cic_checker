from django.urls import path

from apps.cic_tool.views import SingleView, MultipleView

app_name = "tool"
urlpatterns = [
    path("single-checks/", SingleView.as_view(), name="single"),
    path("multiple-checks/", MultipleView.as_view(), name="multiple"),
]
