import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('Mall_Customers.csv')
data = pd.get_dummies(data, columns=['CustomerID', 'Gender', 'Age'])
# Preprocessing
# [Insert preprocessing steps here]

# Selecting features and normalization
# [Insert feature selection and normalization steps here]

# KMeans Clustering
kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0).fit(data)

#kmeans = KMeans(n_clusters=5, random_state=0).fit(data)
data['Cluster'] = kmeans.labels_

# Plotting
sns.scatterplot(data=data, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster')
plt.title('Customer Segments')
plt.show()
