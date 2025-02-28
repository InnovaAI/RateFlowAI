from django.urls import path
from .views import predictRate

urlpatterns = [
    path('predict/<str:baseCurrency>/<str:targetCurrency>/', predictRate),
]