from django.shortcuts import render
#804DDCE9-9BBE-45DE-A5F2-BCA7D4C58400
# Create your views here.
from rest_framework import viewsets, mixins

from .models import ChangeModel, CurrencyModel
from .serializers import ChangeSerializer, CurrencySerializer



class ChangeViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = ChangeModel.objects.all()
    serializer_class = ChangeSerializer

class CurrencyViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = CurrencyModel.objects.all()
    serializer_class = CurrencySerializer

