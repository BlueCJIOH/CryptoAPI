from abc import ABC

from rest_framework import serializers

from .models import ChangeModel, CurrencyModel


class ExchangeSerializer(serializers.Serializer):
    name = serializers.CharField()

# class CurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CurrencyModel
#         fields = '__all__'
#
#
# class ChangeSerializer(serializers.ModelSerializer):
#     currencies = CurrencySerializer(many=True, read_only=True)
#
#     class Meta:
#         model = ChangeModel
#         fields = ['name', 'currencies']
