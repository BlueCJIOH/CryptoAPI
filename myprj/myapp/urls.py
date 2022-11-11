from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import ChangeViewSet, CurrencyViewSet

router = SimpleRouter()
router.register(r'changes', ChangeViewSet)
router.register(r'currencies', CurrencyViewSet)

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
    path('', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
