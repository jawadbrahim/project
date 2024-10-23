import abc

class AstractionDataAccess(metaclass=abc.ABCMeta):
    def create_phone(self):
        raise NotImplementedError()
    def get_phone(self):
        raise NotImplementedError()
    def create_phonenumber(self):
        raise NotImplementedError()
    def celete_phone_number(self):
        raise NotImplementedError()