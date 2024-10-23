from ..setting.development import Development
from ..setting.options import ResponseSerializeOption
from .response_json import Responsejson

class FactoryResponseJson:
    @staticmethod
    def build_object(service=Development.RESPONSE_SERIALIZE):
        if service == ResponseSerializeOption.PYDANTIC_JSON:
            return Responsejson()
        raise NotImplementedError()