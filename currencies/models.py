from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ExchangeRate(models.Model):
    baseCurrency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="baseRates")
    targetCurrency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="targetRates")
    rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CustomExchangeRate_{self.baseCurrency.name}_to_{self.targetCurrency.name}"

    class Meta:
        ordering = ["-timestamp"]