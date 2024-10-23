from dataclasses import dataclass
import uuid
from datetime import datetime

@dataclass
class AuthCreated:
    id:uuid.UUID
    phone_number:str
    replied_phone_number:str
    created_at:datetime
    token:str
    