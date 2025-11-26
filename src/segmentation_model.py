from sklearn.cluster import KMeans
import pandas as pd

def segment_stores(df):
    store_summary = df.groupby('Store_ID').agg({
        'Revenue': ['mean', 'std', 'sum']
    })
    store_summary.columns = ['avg_sales', 'std_sales', 'total_sales']

    kmeans = KMeans(n_clusters=3, random_state=42)
    store_summary['cluster'] = kmeans.fit_predict(store_summary)
    return store_summary.reset_index()