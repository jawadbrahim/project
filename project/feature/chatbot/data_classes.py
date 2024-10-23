from dataclasses import dataclass

from datetime import datetime
@dataclass
class Create_Qa:
   
    answer:str
    phone_number:str
    replied_phone_number:str
    created_at:datetime
    token_cost:float