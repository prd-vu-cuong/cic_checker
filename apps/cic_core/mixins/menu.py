#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/29/22, 8:09 PM"
#
from apps.cic_core.services.menu import MenuService
from django.views.generic import TemplateView


class MenuMixin(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
