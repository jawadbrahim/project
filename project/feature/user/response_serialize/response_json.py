from .response_Serialze_model import UserSerialize
from ..data_classes import UserCreated
from .abstraction import AbstractionResponse

class Responsejson(AbstractionResponse):
    def serialze_create_user(self,user):
        user_data=UserCreated(
            id=user.id,
            name=user.name,
            created_at=user.created_at

        )
        response=UserSerialize(user=user_data)
        return response.json()
        