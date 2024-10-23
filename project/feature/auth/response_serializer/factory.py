from ..setting.option import ResponseSerializerOption
from ..setting.development import Development
from .response_json import Response_Json


class FactorySerialize():
    @staticmethod
    def build_object(service=Development.RESPONSE_SERIALIZER):
        if service == ResponseSerializerOption.PYDANTC_JSON:
            return Response_Json()
        raise NotImplementedError()