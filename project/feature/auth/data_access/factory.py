from ..setting.option import OrmSqlAlchemyOption
from ..setting.development import Development
from .orm_sqlachemy import OrmSqlachemy


class FactoryDataAccess():
    @staticmethod
    def build_object(service=Development.ORM_SQLALCHEMY):
        if service==OrmSqlAlchemyOption.ORMSQLACHEMY:
            return OrmSqlachemy()
        raise NotImplementedError()