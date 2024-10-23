from .abstraction import AbstractionDataAccess
from project.module.ormsqlachemy import Orm
from project.model.qa import Qa
from ..data_classes import Create_Qa


class OrmSqlachemy(AbstractionDataAccess, Orm):
    def form_qa(self, qa):
        return Create_Qa(
            id=qa.id,
            question=qa.question,
            answer=qa.answer,
            created_at=qa.created_at,
            token_cost=qa.token_cost,
            phone_number=qa.phone_number, 
            token=qa.token,
            replied_phone_number=qa.replied_phone_number
        )
        
    def Create_Qa(self, question, answer, token_cost, phone_number, token, replied_phone_number):
        qa = Qa(
            question=question,
            answer=answer,
            token_cost=token_cost,
            phone_number=phone_number,
            token=token,
            replied_phone_number=replied_phone_number
        )
        self.add(qa)
        return qa



        
        