from project.decorator.validate import validate_schema
from .request_validator_models import RequestModels
from .abstraction import AbstractionRequestValidator

class RequestValidator(AbstractionRequestValidator):
    def validate_create_user(self):
        return validate_schema(json_schema=RequestModels)
        