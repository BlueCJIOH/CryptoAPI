from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ChangeViewSet, CurrencyViewSet

router = SimpleRouter()
router.register(r'changes', ChangeViewSet)
router.register(r'currencies', CurrencyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
