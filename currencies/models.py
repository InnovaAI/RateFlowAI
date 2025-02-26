from django.db import models

class Currencies(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)

class ExchangeRate(models.Model):
    baseCurrency = models.ForeignKey(Currencies, on_delete=models.CASCADE, related_name="baseRates")
    targetCurrency = models.ForeignKey(Currencies, on_delete=models.CASCADE, related_name="targetRates")
    rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]