from .data_access.factory import FactoryDataAccess
from .user_service.factory import FactoryUserService
from .response_serialize.factory import FactoryResponseJson
from .exception import FailedToCreateUser
from flask import jsonify
class UserController:
    def __init__(self):
        self.data_access=FactoryDataAccess.build_object()
        self.user_service=FactoryUserService.build_object(self.data_access)
        self.response_serializer=FactoryResponseJson.build_object()
    

    def create_user(self,validate_data):
    
     try:
         user=self.user_service.create_user(validate_data.name)
         self.data_access.commit()
         return self.response_serializer.serialze_create_user(user)
     except(FailedToCreateUser,Exception) as e:
        return jsonify({"error":e.to_dict()})


    