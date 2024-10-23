from dataclasses import dataclass
import uuid
from datetime import datetime
@dataclass
class UserCreated:
    id:uuid.UUID
    name:str
    created_at:datetime
    