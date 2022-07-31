#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/30/22, 8:41 PM"
#


class CommonViewMixin:
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)

        return data
