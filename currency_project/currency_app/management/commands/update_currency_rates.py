from django.core.management.base import BaseCommand
import requests
from datetime import datetime
from currency_app.models import Currency, CurrencyRate

class Command(BaseCommand):
    help = 'Update currency rates from API'

    def handle(self, *args, **kwargs):
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()

        for currency_data in data['Valute'].values():
            currency, created = Currency.objects.get_or_create(
                char_code=currency_data['CharCode'],
                name=currency_data['Name']
            )
            date = datetime.strptime(data['Date'], '%Y-%m-%dT%H:%M:%S%z').date()
            CurrencyRate.objects.update_or_create(
                currency=currency,
                date=date,
                defaults={'value': currency_data['Value']}
            )
        self.stdout.write(self.style.SUCCESS('Currency rates updated successfully'))
