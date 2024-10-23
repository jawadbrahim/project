from ..data_classes import UserCreated
from pydantic import BaseModel
class UserSerialize(BaseModel):
    user:UserCreated