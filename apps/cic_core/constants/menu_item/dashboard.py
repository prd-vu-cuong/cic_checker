#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/29/22, 9:15 PM"
#
from apps.cic_core.constants.base import BaseFeature
from apps.cic_core.constants.base.feature_keys import FeatureKey


class DashBoard(BaseFeature):
    _KEY = FeatureKey.DASH_BOARD
    _NAME = "Dashboard"
    _ICON = "icon-speedometer menu-icon"
    _URL = "/"
