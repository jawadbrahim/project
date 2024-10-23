import abc

class AbstractionSeriliazer(metaclass=abc.ABCMeta):
    def serialize_auth(self):
        raise NotImplementedError()