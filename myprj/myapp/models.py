from django.db import models


# Create your models here.


class ChangeModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CurrencyModel(models.Model):
    name = models.CharField(max_length=10)
    value = models.FloatField()
    change = models.ForeignKey(ChangeModel, on_delete=models.CASCADE, related_name='currencies')

    def __str__(self):
        return self.name
