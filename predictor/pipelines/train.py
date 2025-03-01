import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from currencies.models import ExchangeRate
import joblib
import os


def trainUsdToTshModel():
    # Fetch data from DB
    rates = ExchangeRate.objects.filter(
        baseCurrency__code='USD',
        targetCurrency__code='TZS'
    ).order_by('timestamp').values('timestamp', 'rate')

    df = pd.DataFrame(rates).set_index('timestamp')

    # Train ARIMA model
    model = ARIMA(df['rate'], order=(5, 1, 0))  # (p,d,q) parameters
    modelFit = model.fit()

    # Save model
    modelDir = 'predictor/models/USD_TSH'
    os.makedirs(modelDir, exist_ok=True)
    joblib.dump(modelFit, f'{modelDir}/arima_model.joblib')

    return modelFit