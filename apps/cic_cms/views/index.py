#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/30/22, 9:20 PM"
#
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from apps.cic_core.mixins.base import BaseViewMixin


class IndexView(BaseViewMixin, generic.TemplateView):
    def dispatch(self, request, *args, **kwargs):
        is_authenticated = request.user and request.user.is_authenticated
        redirect_url = reverse_lazy("cms:dashboard")
        if not is_authenticated:
            redirect_url = reverse_lazy("login")

        return HttpResponseRedirect(redirect_url)
