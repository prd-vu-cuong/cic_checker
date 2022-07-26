#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuong"
#  __date_time = "7/24/22, 10:32 AM"

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from re import search


class AuthRequiredMiddleware(MiddlewareMixin):
    def __int__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        if not search("/admin/", request.path):
            if not request.user.is_authenticated and request.path != reverse("login"):
                return HttpResponseRedirect(redirect_to=(reverse("login")))

        response = self.get_response(request)
        return response
