import jwt
import traceback

from django.utils.functional import SimpleLazyObject
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from django.conf import LazySettings
from django.http import HttpResponse
settings = LazySettings()


class JWTAuthMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        return None
        if request.path.startswith('/login') or request.path.startswith('/register'):
            return None
        token = request.META.get('HTTP_AUTHORIZATION', None)
        
        if token is not None:
            try:
                payload = jwt.decode(token, '123456', algorithms=['HS256'])
                request.user = User.objects.get(username=payload['username'])
            except (jwt.DecodeError, User.DoesNotExist):
                return HttpResponse("invalid_token", status=401)
            except jwt.ExpiredSignatureError:
                return HttpResponse("expired_token", status=401)
            except Exception as e: 
                return HttpResponse("Unauthorized", status=401)
        else:
            return HttpResponse("Unauthorized", status=401)
