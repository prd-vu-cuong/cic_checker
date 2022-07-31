#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/28/22, 11:08 PM"
#
from apps.cic_core.constants.base import BaseFeature
from apps.cic_core.constants.base.feature_keys import FeatureKey


class CicAccount(BaseFeature):
    _KEY = FeatureKey.CIC_ACCOUNT
    _NAME = "Tài Khoản CIC"
    _ICON = "icon-settings menu-icon"
    _URL = "/accounts"
