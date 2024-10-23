from ..setting.development import Development
from ..setting.options import RequestValidatorOption
from .request_validator import RequestValidator

class FactoryRequestValidator():
    @staticmethod
    def build_object(service=Development.REQUEST_VALIDATOR):
        if service ==RequestValidatorOption.PYDANTIC_MODEL:
            return RequestValidator()
        raise NotImplementedError()