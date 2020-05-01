import jwt


from django.contrib.auth.models import User

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication


class JSONWebTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, '123456')
            user = User.objects.get(username=payload['username'])
        except (jwt.DecodeError, User.DoesNotExist):
            raise exceptions.AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        return (user, payload)