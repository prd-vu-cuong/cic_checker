#  Copyright (c) 2022,
#  CIC Checker
#  __author = "cuongvu"
#  __date_time = "7/30/22, 8:47 PM"
#


class CicCoreUtils:
    @staticmethod
    def get_template_name(name: str, request: {} = None):
        if not request:
            return None

        suffix = ".html"
        if name.endswith(suffix):
            suffix = ""

        return f"{name}{suffix}"
