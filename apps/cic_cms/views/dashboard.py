#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/30/22, 9:11 PM"
#

from django.views import generic

from apps.cic_cms.views import BaseCmsView


class DashboardView(BaseCmsView, generic.TemplateView):
    template_name = "cic_cms/dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        return data

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        return response
