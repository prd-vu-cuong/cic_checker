#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/28/22, 11:03 PM"
from apps.cic_core.constants.base import BaseFeature
from apps.cic_core.constants.base.feature_keys import FeatureKey


class SingleCheck(BaseFeature):
    _KEY = FeatureKey.SINGLE_CHECK
    _NAME = "Check Đơn"
