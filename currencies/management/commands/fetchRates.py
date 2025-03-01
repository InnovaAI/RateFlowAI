import os
from django.core.management.base import BaseCommand
from currencies.models import Currency, ExchangeRate
import requests
from django.utils import timezone


class Command(BaseCommand):
    help = "Fetches USD-TSH exchange rates from Alpha Vantage API"

    def handle(self, *args, **kwargs):
        # Get or create USD and TZS currencies
        usd, _ = Currency.objects.get_or_create(code='USD', defaults={'name': 'US Dollar'})
        tzs, _ = Currency.objects.get_or_create(code='TZS', defaults={'name': 'Tanzanian Shilling'})

        # Fetch rates from Alpha Vantage (replace with your API key)
        ApiKey = os.getenv('ALPHA_VANTAGE_API_KEY')  # Use .env file for real projects
        url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=USD&to_symbol=TZS&apikey={ApiKey}"
        
        response = requests.get(url)
        data = response.json()

        if 'Time Series FX (Daily)' not in data:
            self.stdout.write(self.style.ERROR("Failed to fetch data. Check API key or usage limits."))
            return

        # Save latest 30 days of data
        for dateStr, dailyData in list(data['Time Series FX (Daily)'].items())[:30]:
            rate = float(dailyData['4. close'])
            timestamp = timezone.datetime.strptime(dateStr, "%Y-%m-%d")
            
            ExchangeRate.objects.update_or_create(
                baseCurrency=usd,
                targetCurrency=tzs,
                timestamp=timestamp,
                defaults={'rate': rate}
            )

        self.stdout.write(self.style.SUCCESS("Successfully updated USD-TSH rates!"))