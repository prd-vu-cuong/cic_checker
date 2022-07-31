#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/29/22, 8:26 PM"
#

try:
    from threading import local
except ImportError:
    # noinspection PyUnresolvedReferences
    from django.utils._threading_local import local

cic_global = local()
