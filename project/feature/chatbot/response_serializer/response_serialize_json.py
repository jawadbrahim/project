from .abstraction import AbstarctionResponseSeraizlier
from .response_model import SerailzeModel
from ..data_classes import Create_Qa

class Response_json(AbstarctionResponseSeraizlier):
    def Serialize_ChatBot(self, qa):
     qa_data = Create_Qa(
        phone_number=qa.phone_number,
        replied_phone_number=qa.replied_phone_number,
        answer=qa.answer,
        created_at=qa.created_at,
        token_cost=qa.token_cost
     )
     response = SerailzeModel(qa=qa_data)
     return response.json()

        