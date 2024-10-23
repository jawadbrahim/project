from database.postgres import db
from dataclasses import dataclass
import uuid
from sqlalchemy.dialects.postgresql import UUID
import datetime
import pytz

from sqlalchemy.orm import relationship

@dataclass
class Auth(db.Model):
    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    replied_phone_number=db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.now(pytz.timezone('GMT')))
    token_id = db.Column(UUID(as_uuid=True), db.ForeignKey("token.id"), unique=True)
    

