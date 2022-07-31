#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/30/22, 9:07 PM"
#
from apps.cic_core.constants.menu import SUPER_ADMIN_MENU


class CmsService:
    @classmethod
    def get_init_data(cls):
        return dict(
            text="Hello",
            products=[
                dict(id=1, name="Số Lần Check", count=4565),
                dict(id=2, name="Số CIC Đã Check", count=4565),
            ],
            menu_items=SUPER_ADMIN_MENU,
        )
