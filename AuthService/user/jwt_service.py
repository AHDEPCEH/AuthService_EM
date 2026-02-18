import uuid
import datetime

import jwt
from django.conf import settings

from AuthService.user.models import RevokeToken, User


class JwtService:

    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.expire = settings.TOKEN_EXPIRE
        self.algorithm = "HS256"

    def generate_token(self, user) -> str:
        payload = {
            "user_id": user.id,
            "email": user.email,
            "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=self.expire),
            "iat": datetime.datetime.now(datetime.UTC),
            "jti": str(uuid.uuid4())
        }

        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def get_token_payload(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.InvalidTokenError:
            return None

        if RevokeToken.objects.filter(jti=payload.get("jti")).exists():
            return None

        if datetime.datetime.now(datetime.UTC) > datetime.datetime.fromtimestamp(payload.get("exp")):
            return None

        user_id = payload.get("user_id")

        if User.objects.get(id=user_id):
            return payload
        return None

    def revoke_token(self, token):
        payload = self.get_token_payload(token)
        if payload is not None:
            revoke_token = RevokeToken(
                jti=payload.get("jti"),
                user_id=payload.get("user_id"),
                expired_at=datetime.datetime.fromtimestamp(payload.get("exp")))
            revoke_token.save()
        #Нужна ошибка