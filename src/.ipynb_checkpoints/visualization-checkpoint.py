import seaborn as sns
import matplotlib.pyplot as plt

def plot_sales_trends(df):
    plt.figure(figsize=(12,6))
    sns.lineplot(x='Date', y='Revenue', data=df, hue='Store_ID')
    plt.title('Store-wise Revenue Over Time')
    plt.show()

def plot_seasonality(df):
    monthly_sales = df.groupby('Month')['Revenue'].sum()
    plt.figure(figsize=(8,4))
    sns.barplot(x=monthly_sales.index, y=monthly_sales.values)
    plt.title("Monthly Seasonality")
    plt.show()