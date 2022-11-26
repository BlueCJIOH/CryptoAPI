from django.shortcuts import render
# 804DDCE9-9BBE-45DE-A5F2-BCA7D4C58400
# Create your views here.
from rest_framework import viewsets, mixins, views
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from .serializers import ExchangeSerializer
from .services.services import get_all_exchanges, get_exchange_by_name


class ExchangeViewSet(GenericViewSet):
    serializer_class = ExchangeSerializer
    exchanges = (
        'Binance',
        'Bybit',
    )

    def list(self, request):
        return Response([{el[0]: el[1]} for el in tuple(zip(['name', ] * len(self.exchanges), self.exchanges))])

    @action(detail=False, methods=['get'], url_path='get_all_currencies')
    def get_all_currencies(self, request):
        content = [{'Binance': get_all_exchanges()['Binance']}, {'Bybit': get_all_exchanges()['Bybit']}]
        return Response(content)

    @action(detail=False, methods=['post'], url_path='get_currencies_by_name', )
    def get_currencies_by_name(self, request):
        return Response({request.data['name']: get_exchange_by_name(request.data['name'].lower())})
