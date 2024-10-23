from pydantic import BaseModel

class AuthModel(BaseModel):
    phone_number:str
    replied_phone_number:str