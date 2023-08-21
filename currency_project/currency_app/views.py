from django.shortcuts import render

from datetime import datetime

from .models import CurrencyRate


def show_rates(request):
    date_str = request.GET.get('date')
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            rates = CurrencyRate.objects.filter(date=date)
        except ValueError:
            rates = []
            date = None
    else:
        rates = []
        date = None

    return render(request, 'show_rates.html', {'rates': rates, 'date': date})
