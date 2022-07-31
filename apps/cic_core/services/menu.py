#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/29/22, 8:12 PM"
#
from apps.cic_core.authentications import get_current_request
from apps.cic_core.constants.menu import SUPER_ADMIN_MENU


class MenuService:
    def generate_dynamic_menu(self, **kwargs):
        request = get_current_request()
        print(request)
        return SUPER_ADMIN_MENU
