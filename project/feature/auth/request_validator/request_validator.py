from project.decorator.validate import validate_schema
from.abstraction import AbstractionRequestValidator
from .request_validatory_models import AuthModel


class ReqeustValidator(AbstractionRequestValidator):
    def validate_auth(self):
        return validate_schema(json_schema=AuthModel)