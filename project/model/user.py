from database.postgres import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime
import pytz

@dataclass

class User(db.Model):
    id=db.Column(UUID(as_uuid=True),default=uuid.uuid4,primary_key=True)
    name=db.Column(db.String(20))
    created_at=db.Column(db.DateTime,default=datetime.datetime.now(pytz.timezone("GMT")))