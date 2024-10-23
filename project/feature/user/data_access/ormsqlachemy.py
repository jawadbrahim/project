from project.model.user import User
from project.module.ormsqlachemy import Orm
from .abstraction import AbstractionDataAccess

class OrmSqlAlchemy(AbstractionDataAccess,Orm):

    def create_user(self,name):
        user=User(name=name)
        self.add(user)
        return user
    

        