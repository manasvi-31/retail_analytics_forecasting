import streamlit as st
import pandas as pd
from src.forecasting_model import forecast_sales
from src.segmentation_model import segment_stores
from src.visualization import plot_sales_trends

st.title("🧭 Retail Analytics & AI Forecasting Dashboard")

df = pd.read_csv('data/Retail_Sales_Data_Unlox.csv')
df['Date'] = pd.to_datetime(df['Date'])
stores = df['Store_ID'].unique()

# Sidebar
selected_store = st.sidebar.selectbox("Select Store:", stores)

# Show Forecast
st.subheader(f"📊 Forecast for {selected_store}")
forecast = forecast_sales(df, selected_store)
st.line_chart(forecast.set_index('ds')[['yhat']])

# Segmentation section
st.subheader("🧩 Store Segmentation")
segments = segment_stores(df)
st.dataframe(segments)