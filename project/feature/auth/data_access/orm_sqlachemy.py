from project.model.auth import Auth
from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import Orm
from project.model.token import Token


class OrmSqlachemy(AbstractionDataAccess,Orm):

    def create_auth(self,phone_number,replied_phone_number):
        auth=Auth(
            phone_number=phone_number,
            replied_phone_number=replied_phone_number
        )
        self.add(auth)
        return auth
    def number_exists(self,phone_number):
        number_exists=Auth.query.filter(Auth.phone_number==phone_number).first()
        return number_exists
    def insert_token(self,token_id,token_str):
        token=Token(
            id=token_id,
            token=token_str
        )
        self.add(token)
        return token
    def update_token_id(self,auth_id,token_id):
        auth_record=Auth.query.filter(Auth.id==auth_id).first()
        if auth_record:
            auth_record.token_id=token_id
            self.commit()
        return auth_record