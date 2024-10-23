from ..setting.option import DefaultOption
from ..setting.development import Development
from .default import Default
class FactoryService():
    @staticmethod
    def build_object(data_access,service=Development.AUTH_SERVICE):
        if service == DefaultOption.DEFAULT:
            return Default(data_access)
        raise NotImplementedError()