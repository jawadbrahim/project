from database.postgres import db
from dataclasses import dataclass
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime
import pytz

@dataclass
class Token(db.Model):
    id = db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    token=db.Column(db.String(200))
    created_at=db.Column(db.DateTime,default=lambda:datetime.datetime.now(pytz.timezone('GMT')))
    user_id=db.Column("user_id",UUID(as_uuid=True),db.ForeignKey("user.id"))
    
    

