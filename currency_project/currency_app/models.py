from django.db import models

# Create your models here.


class Currency(models.Model):
    char_code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CurrencyRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField()

    class Meta:
        unique_together = ['currency', 'date']
