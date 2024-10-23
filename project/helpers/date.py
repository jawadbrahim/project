from datetime import timedelta,datetime
import pytz

class DateHelper:
    @staticmethod
    def get_expiration_date(minutes=60):
        exp=datetime.utcnow()+ timedelta(minutes=minutes)
        return exp

