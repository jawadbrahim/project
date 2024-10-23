from dataclasses import dataclass
from project.config.development import Development
@dataclass
class Config:
    JWT_SECRET=Development.JWT_SECRET
    JWT_DURATION=60
    JWT_SIGN_ALGORITHM='HS256'