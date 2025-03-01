from django.core.management.base import BaseCommand
from currencies.models import Currency


class Command(BaseCommand):
    help = 'Seed initial currencies'

    def handle(self, *args, **kwargs):
        currencies = [
            {'code': 'USD', 'name': 'US Dollar'},
            {'code': 'TZS', 'name': 'Tanzanian Shilling'},
            {'code': 'EUR', 'name': 'Euro'},
        ]
        for curr in currencies:
            Currency.objects.get_or_create(**curr)
        self.stdout.write("Currencies seeded successfully!")