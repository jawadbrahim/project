from pydantic import BaseModel
from ..data_classes import AuthCreated
class AuthModel(BaseModel):
    auth:AuthCreated