import jwt
import traceback

from django.utils.functional import SimpleLazyObject
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser, User
from django.conf import LazySettings
from django.contrib.auth.middleware import get_user

settings = LazySettings()


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = SimpleLazyObject(lambda: self.__class__.get_jwt_user(request))
        if request.user is none:
            return HttpResponse("Invalid token", status=401)
    @staticmethod
    def get_jwt_user(request):

        user_jwt = get_user(request)
        if user_jwt.is_authenticated():
            return user_jwt
        token = request.META.get('HTTP_AUTHORIZATION', None)
        
        if token is not None:
            try:
                payload = jwt.decode(token, '123456')
                user = User.objects.get(email=payload['email'])
                return user
            except Exception as e: # NoQA
                traceback.p
        return None