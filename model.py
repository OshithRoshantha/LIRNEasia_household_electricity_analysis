import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import silhouette_score
from sklearn.impute import SimpleImputer

df = pd.read_csv(r"C:\Users\OSHITH\OneDrive - University of Kelaniya\Desktop\lirneasia\houseConsumption.csv")

numeric_cols = df.select_dtypes(include=[np.number]).columns
df_numeric = df[numeric_cols]

imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df_numeric), columns=numeric_cols)

df[numeric_cols] = df_imputed

features = df[['TOTAL_IMPORT (kWh)', 'floor_area', 'total_monthly_expenditure_of_last_month', 'no_of_household_members']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method For Optimal K')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=42)
y_kmeans = kmeans.fit_predict(scaled_features)

df['Cluster'] = y_kmeans

sns.scatterplot(x=df['TOTAL_IMPORT (kWh)'], y=df['total_monthly_expenditure_of_last_month'], hue=df['Cluster'], palette='Set1')

plt.title('K-means Clustering')
plt.xlabel('TOTAL_IMPORT (kWh)')
plt.ylabel('Total Monthly Expenditure of Last Month')
plt.show()

centroids = pd.DataFrame(kmeans.cluster_centers_, columns=['TOTAL_IMPORT (kWh)', 'floor_area', 'total_monthly_expenditure_of_last_month', 'no_of_household_members'])
print("Centroids of clusters:\n", centroids)

print("Cluster distribution:\n", df['Cluster'].value_counts())

sil_score = silhouette_score(scaled_features, y_kmeans)
print(f"Silhouette Score: {sil_score}")
