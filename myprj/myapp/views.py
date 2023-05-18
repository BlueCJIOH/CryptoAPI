# 804DDCE9-9BBE-45DE-A5F2-BCA7D4C58400
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import ExchangeSerializer, CurrencySerializer, ExchangeCurrencySerializer
from .services.services import get_all_exchanges, get_exchange_by_name, \
    get_bybit_by_currency, get_binance_by_currency, get_exchange_by_currency, get_names_from_exchange, \
    get_names_from_exchanges


class ExchangeViewSet(GenericViewSet):
    exchanges = (
        'Binance',
        'Bybit',
    )
    default_serializer_class = ExchangeSerializer
    serializer_classes = {
        'list': CurrencySerializer,
        'all_currencies': CurrencySerializer,
        'currencies_by_name': ExchangeSerializer,
        'all_currency_by_name': CurrencySerializer,
        'currency_names_from': ExchangeSerializer,
        'currency_by_name_from': ExchangeCurrencySerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def list(self, request):
        return Response([{el[0]: el[1]} for el in tuple(zip(['name', ] * len(self.exchanges), self.exchanges))])

    @action(detail=False, methods=['get'], url_path='all_currencies')
    def all_currencies(self, request):
        content = [{'Binance': get_all_exchanges()['Binance']}, {'Bybit': get_all_exchanges()['Bybit']}]
        return Response(content)

    @action(detail=False, methods=['post'], url_path='currencies_by_name')
    def currencies_by_name(self, request):
        return Response({request.data['name']: get_exchange_by_name(request.data['name'].lower())})

    @action(detail=False, methods=['post'], url_path='all_currency_by_name')
    def all_currency_by_name(self, request):
        content = [{'Binance': get_bybit_by_currency(request.data['cname'].upper())},
                   {'Bybit': get_binance_by_currency(request.data['cname'].upper())}]
        return Response(content)

    @action(detail=False, methods=['post'], url_path='currency_by_name_from')
    def currency_by_name_from(self, request):
        return Response(
            {request.data['name']: get_exchange_by_currency(request.data['name'].lower(), request.data['cname'].upper())})

    @action(detail=False, methods=['post'], url_path='currency_names_from')
    def currency_names_from(self, request):
        return Response({request.data['name']: get_names_from_exchange(request.data['name'].lower())})

    @action(detail=False, methods=['get'], url_path='all_currency_names')
    def all_currency_names(self, request):
        return Response(get_names_from_exchanges())