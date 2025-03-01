from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from predictor.pipelines.train import trainUsdToTshModel
import joblib


@api_view(['GET'])
def predictRate(request, baseCurrency, targetCurrency):
    if baseCurrency != 'USD' or targetCurrency != 'TZS':
        return Response({"error": "Only USD-TSH supported now"}, status=400)

    # Load model
    modelPath = 'predictor/models/USD_TSH/arima_model.joblib'
    model = joblib.load(modelPath)

    # Predict next 7 days
    forecast = model.forecast(steps=7)
    return Response({
        'forecast': forecast.tolist(),
        'currency_pair': f'{baseCurrency}-{targetCurrency}'
    })
