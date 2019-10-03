import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans

#Generating the graph containing 4 blobs
from sklearn.datasets.samples_generator import make_blobs
X,Y_true = make_blobs(n_samples = 400, centers = 4, cluster_std = 0.60, random_state = 0)

#Creating a visual od the dataset
plt.scatter(X[:,0], X[:,1], s = 20);
plt.show()

#make an object of KMean and Training the model + make prediction
kmeans = KMeans(n_clusters= 4)
kmeans.fit(X)
Y_kmeans = kmeans.predict(X)

#Plotting and visualizing the clusters' centers picked by K_means Python estmator
from sklearn.datasets.samples_generator import make_blobs
X,Y_true = make_blobs(n_samples = 400, centers = 4, cluster_std = 0.60, random_state = 0)

plt.scatter(X[:,0], X[:,1], c=Y_kmeans , s = 20, cmap= 'summer')
centers= kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='blue', s = 100, alpha = 0.9)
plt.show()