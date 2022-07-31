#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/30/22, 8:40 PM"
#

from apps.cic_core.mixins.common import CommonViewMixin
from apps.cic_core.services.utils import CicCoreUtils


class BaseViewMixin(CommonViewMixin):
    template_name = ""

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, *kwargs)

        return data

    def dispatch(self, request, *args, **kwargs):
        self.template_name = CicCoreUtils.get_template_name(self.template_name, request)

        return super().dispatch(request, *args, **kwargs)
