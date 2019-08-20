import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans as km

data = pd.read_csv('Datasets/Distribution-1.csv')
data = data[['ypos','xpos']]

x = data.to_numpy()

kmeans = km(n_clusters=2)
kmeans.fit(x)
kmeans.cluster_centers_
plt.scatter(x[ : , 0], x[ : , 1], s =50, color='b')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=130,c='r',marker = 'x')
plt.show()