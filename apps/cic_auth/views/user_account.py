#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/31/22, 12:30 PM"
#
from django.views import generic

from apps.cic_cms.views import BaseCmsView


class UserManageView(BaseCmsView, generic.TemplateView):
    template_name = "cic_auth/account-manage.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
