import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
print("Loading dataset...")
data = pd.read_csv('data.csv/data.csv', encoding='ISO-8859-1')
print(f"Dataset loaded! Rows: {data.shape[0]}, Columns: {data.shape[1]}")

# 2. Data Cleaning
data = data.dropna(subset=['CustomerID'])
data['CustomerID'] = data['CustomerID'].astype(int).astype(str)
data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]
data['TotalAmount'] = data['Quantity'] * data['UnitPrice']

# 3. Create RFM Dataframe
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
reference_date = data['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = data.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalAmount': 'sum'
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']
print("RFM metrics engineered successfully!")

# 4. Data Transformation & Scaling
features = ['Recency', 'Frequency', 'Monetary']
X = rfm[features]
X_log = np.log1p(X)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_log)

# 5. Finding Optimal Clusters (Elbow Method)
print("Calculating Elbow Curve values...")
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# 6. Plot the Elbow Graph
plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.grid(True)
plt.show()

# 7. ASSIGN CLUSTERS & EXPORT FOR POWER BI
# ==========================================
print("\nAssigning clusters...")
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
rfm['Cluster'] = kmeans.fit_predict(X_scaled)

print("\n--- Final Cluster Profiles ---")
cluster_profile = rfm.groupby('Cluster')[features].mean().round(2)
print(cluster_profile)

# Bring back the Country column
customer_countries = data[['CustomerID', 'Country']].drop_duplicates(subset=['CustomerID'])
final_segmented_data = rfm.reset_index().merge(customer_countries, on='CustomerID', how='left')

# Save the CSV file
final_segmented_data.to_csv('segmented_customers.csv', index=False)
print("\n🎉 Success! 'segmented_customers.csv' has been saved and is ready for Power BI.")