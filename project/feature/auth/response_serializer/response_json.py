from .abstraction import AbstractionSeriliazer
from .response_serialize_models import AuthModel
from ..data_classes import AuthCreated

class Response_Json(AbstractionSeriliazer):
    def serialize_auth(self,auth):
        auth_data=AuthCreated(
            id=auth.id,
            phone_number=auth.phone_number,
            replied_phone_number=auth.replied_phone_number,
            created_at=auth.created_at,
            token= auth.token
        )
        response=AuthModel(auth=auth_data)
        return response.json()

        
