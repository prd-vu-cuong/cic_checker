#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/30/22, 8:59 PM"
#
#
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

# Create your views here.
from apps.cic_cms.services import CmsService
from apps.cic_core.mixins.base import BaseViewMixin


class BaseCmsView(BaseViewMixin):
    request = None
    init_data = True

    def check_login(self):
        if not self.request.user or not self.request.user.is_authenticated:
            if self.request.is_ajax():
                return HttpResponseForbidden()
            else:
                return HttpResponseRedirect(reverse("login"))

        return None

    def dispatch(self, request, *args, **kwargs):
        self.request = request

        check = self.check_login()
        if check is not None:
            return check

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        init_data = CmsService.get_init_data()

        for k, v in init_data.items():
            context_data[k] = v

        return context_data
