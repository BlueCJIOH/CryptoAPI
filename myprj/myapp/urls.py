from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import ExchangeViewSet

router = DefaultRouter()
router.register(r'exchanges', ExchangeViewSet, basename='exchanges')

schema_view = get_schema_view(
    openapi.Info(
        title="Crypto API",
        default_version='v1',
        description="All changes with crypto currencies",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('exchanges/', ExchangeViewSet.as_view({'get': 'list'})),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls
