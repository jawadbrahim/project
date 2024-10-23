from .abstraction import AbstractionUserservice
from ..exception import FailedToCreateUser
class Default(AbstractionUserservice):
    def __init__(self,data_access):
        self.data_access=data_access

    def create_user(self,name):
        user=self.data_access.create_user(name)
        if not user:
            raise FailedToCreateUser(name=name)

        return user
        