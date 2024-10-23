from ..setting.option import RequestValidatoroption
from ..setting.development import Development
from .request_validator import ReqeustValidator


class FactoryValidator():
    @staticmethod
    def build_object(service=Development.REQUEST_VALIDATOR):
        if service == RequestValidatoroption.PYDANTIC_MODEL:
            return ReqeustValidator()
        raise NotImplementedError()