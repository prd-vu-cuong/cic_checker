from django.urls import path, include

from apps.cic_auth.views.user_account import UserManageView

urlpatterns = [
    path("", include("apps.cic_cms.urls")),
    path("tools/", include("apps.cic_tool.urls")),
    path("auth/", include("apps.cic_auth.urls")),
    path("api/", include("apps.cic_api.urls")),
    path("user-managements/", UserManageView.as_view(), name="user-management"),
]
