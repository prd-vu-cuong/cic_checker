#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuong"
#  __date_time = "7/24/22, 5:11 PM"
from apps.cic_core.constants.menu import SUPER_ADMIN_MENU


class SingleService:
    @classmethod
    def get_init_data(cls):
        return dict(
            text="Hello",
            products=[
                dict(id=1, name="Products Sold", count=4565),
                dict(id=2, name="Net Profit", count=4565),
                dict(id=3, name="New Customers", count=4565),
                dict(id=4, name="Customer Satisfaction", count=4565),
            ],
            menu_items=SUPER_ADMIN_MENU,
        )
