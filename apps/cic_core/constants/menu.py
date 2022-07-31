#  Copyright (c) 2022,
#  CIC Checker
# __author = "cuongvu"
# __date_time = "7/28/22, 11:00 PM"
from apps.cic_core.constants.menu_item import (
    MultipleCheck,
    SingleCheck,
    User,
    History,
    CicAccount,
    DashBoard,
)

SINGLE_CHECK_MENU = [
    DashBoard,
    SingleCheck,
]

MULTIPLE_CHECK_MENU = [
    DashBoard,
    MultipleCheck,
]

SUPER_ADMIN_MENU = [
    DashBoard,
    User,
    History,
    CicAccount,
    SingleCheck,
    MultipleCheck,
]
