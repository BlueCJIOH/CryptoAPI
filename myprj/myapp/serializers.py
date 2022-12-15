from rest_framework import serializers


class ExchangeSerializer(serializers.Serializer):
    name = serializers.CharField()


class CurrencySerializer(serializers.Serializer):
    cname = serializers.CharField()


class ExchangeCurrencySerializer(serializers.Serializer):
    name = serializers.CharField()
    cname = serializers.CharField()
