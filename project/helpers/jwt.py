import jwt


class JwtHelper:

    def __init__(self,secret,algorithm):
        self.secret=secret
        self.algorithm=algorithm
    def encode(self,payload):
        jwt_encode=jwt.encode(payload,self.secret,algorithm=self.algorithm)
        return jwt_encode
    def decode(self,jwt_encode):
        payload=jwt.decode(jwt_encode,self.secret,algorithm=[self.algorithm])
        return payload