from prophet import Prophet
import pandas as pd

def forecast_sales(df, store_id):
    # Filter store-level data
    store_data = df[df['Store_ID'] == store_id][['Date', 'Revenue']]
    store_data = store_data.rename(columns={'Date': 'ds', 'Revenue': 'y'})
    
    # Create model
    model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
    model.fit(store_data)
    
    # Future dates
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]