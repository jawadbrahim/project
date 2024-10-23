import abc

class AbstractionUserservice(metaclass=abc.ABCMeta):
    def create_user(self):
        raise NotImplementedError()