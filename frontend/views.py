from django.shortcuts import render
from currencies.models import Currency


def dashboard(request):
    # Get active currencies for future dropdowns
    currencies = Currency.objects.filter(isActive=True)
    return render(request, 'dashboard.html', {
        'currencies': currencies  # Pass to template (for extensibility)
    })
