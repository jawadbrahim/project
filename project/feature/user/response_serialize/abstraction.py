import abc
class AbstractionResponse(metaclass=abc.ABCMeta):
    def serialze_create_user(self):
        raise NotImplementedError()
