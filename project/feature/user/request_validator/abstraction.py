import abc

class AbstractionRequestValidator(metaclass=abc.ABCMeta):
    def validate_create_user(self):
        raise NotImplementedError()