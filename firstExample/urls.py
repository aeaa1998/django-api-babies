
from django.urls import include, path
from authentication import views as authViews
from events import views as eventViews
from parents import views as parentViews
from django.conf.urls import url, include as inc
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'events', eventViews.EventsViewSet)
router.register(r'parent', parentViews.ParentsViewSet)
router.register(r'babies', parentViews.BabiesViewSet)
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

urlpatterns = [
    # path('babies/', include('parents.babies-urls')),
    # path('parent/', include('parents.parents-urls')),
    # path('events/', include('events.urls')),
    # path('login', authViews.login, name = "login"),
    path('api/', include(router.urls)),
    url(r'^api-auth/', inc('rest_framework.urls')),
    url(r'^api/login', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token)
]
