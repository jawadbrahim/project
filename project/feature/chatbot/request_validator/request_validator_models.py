from pydantic import BaseModel

class Chat_Bot_Model(BaseModel):
    question: str
    phone_number: str
    token: str
    replied_phone_number: str
