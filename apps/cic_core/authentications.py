#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/29/22, 8:27 PM"
#
from apps.cic_core import cic_global


def get_current_request():
    return getattr(cic_global, "request", None)
