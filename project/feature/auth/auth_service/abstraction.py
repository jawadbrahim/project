import abc
class AbstractionAuthService(metaclass=abc.ABCMeta):
    def auth(self):
        raise NotImplementedError()
    
    