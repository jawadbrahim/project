import abc

class AbstractionRequestValidator(metaclass=abc.ABCMeta):
    def validate_auth(self):
        raise NotImplementedError()