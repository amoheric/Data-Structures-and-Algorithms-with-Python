import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Mall_Customers.csv')
print(data.columns)

data = pd.get_dummies(data, columns=['CustomerID', 'Gender', 'Age'])

# Preprocessing
# Assume the data has columns 'Recency', 'Frequency', 'Monetary' for RFM analysis
scaler = StandardScaler()
# Check current column names in the DataFrame


# If 'Gender' is spelled differently in the columns, update the column name in your script
# For example, if the actual column name is 'gender', then:
[Running] python -u "c:\Users\amohe.000\source\Customer Segmentation Analysis.py"
Index(['CustomerID', 'Gender', 'Age', 'Annual Income (k$)',
       'Spending Score (1-100)'],
      dtype='object')
Traceback (most recent call last):
  File "c:\Users\amohe.000\source\Customer Segmentation Analysis.py", line 20, in <module>
    data_scaled = scaler.fit_transform(data[['CustomerID', 'Gender', 'Age']])
                                       ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\pandas\core\frame.py", line 3899, in __getitem__
    indexer = self.columns._get_indexer_strict(key, "columns")[1]
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Python312\Lib\site-packages\pandas\core\indexes\base.py", line 6114, in _get_indexer_strict
    self._raise_if_missing(keyarr, indexer, axis_name)
  File "C:\Python312\Lib\site-packages\pandas\core\indexes\base.py", line 6175, in _raise_if_missing
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['CustomerID', 'Gender', 'Age'], dtype='object')] are in the [columns]"

[Done] exited with code=1 in 1.731 seconds


data_scaled = scaler.fit_transform(data[['CustomerID', 'Gender', 'Age']])



# Choosing the number of clusters with Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(data_scaled)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Applying KMeans to the dataset with the optimal number of clusters
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(data_scaled)

# Adding clusters to the original data
data['Cluster'] = cluster_labels

# Visualizing the clusters
plt.scatter(data_scaled[cluster_labels == 0, 0], data_scaled[cluster_labels == 0, 1], s=100, c='red', label ='Cluster 1')
plt.scatter(data_scaled[cluster_labels == 1, 0], data_scaled[cluster_labels == 1, 1], s=100, c='blue', label ='Cluster 2')
plt.scatter(data_scaled[cluster_labels == 2, 0], data_scaled[cluster_labels == 2, 1], s=100, c='green', label ='Cluster 3')
plt.title('Clusters of customers')
plt.xlabel('RFM')
plt.ylabel('Frequency')
plt.legend()
plt.show()

