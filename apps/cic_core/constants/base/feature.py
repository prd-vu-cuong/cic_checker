from abc import ABC


class BaseFeature(ABC):
    _KEY = None
    _NAME = ""
    _ICON = ""
    _URL = ""
    _CHILDREN = []

    @classmethod
    def default_rules(cls):
        return True

    @classmethod
    def get_name(cls):
        return cls._NAME

    @classmethod
    def get_icon(cls):
        return cls._ICON

    @classmethod
    def get_key(cls):
        return cls._KEY

    @classmethod
    def get_children(cls):
        return cls._CHILDREN

    @classmethod
    def get_url(cls):
        return cls._URL
