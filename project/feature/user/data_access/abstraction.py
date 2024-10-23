import abc

class AbstractionDataAccess(metaclass=abc.ABCMeta):
    def create_user(self):
        raise NotImplementedError()
    