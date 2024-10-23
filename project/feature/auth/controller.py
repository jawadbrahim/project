from .data_access.factory import FactoryDataAccess
from .response_serializer.factory import FactorySerialize
from .auth_service.factory import FactoryService
from .exception import PhoneNumberExist
from flask import jsonify

class AuthController:
    def __init__(self):
        self.data_access=FactoryDataAccess.build_object()
        self.auth_service=FactoryService.build_object(self.data_access)
        self.response_serializer=FactorySerialize.build_object()
    def auth(self,validate_data):
        try:
          auth=self.auth_service.auth(validate_data.phone_number,validate_data.replied_phone_number)
          self.data_access.commit()
          return self.response_serializer.serialize_auth(auth)
        except(PhoneNumberExist,Exception)as e:
            return jsonify({"error":e.to_dict()})
