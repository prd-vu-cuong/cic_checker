from abc import ABC


class BaseFeature(ABC):
    _KEY = None
    _NAME = ""
    _CHILDREN = []

    @classmethod
    def default_rules(cls):
        return True
