import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

colors=["r","g","c","b","k",'m']
cluster_names = ['Cluster 1','Cluster 2','Cluster 3','Cluster 4','Cluster 5','Cluster 6']

cluster_num = 2
# clusters = int(input())
tolerance = 0.0001
# tolerance = float(input())
max_iterations = 500
# max_iterations = int(input())


df = pd.read_csv('Datasets/Distribution-1.csv')
df = df[['ypos','xpos']]

x = df.to_numpy()

# print(x)

centroids = {}

for i in range(cluster_num):
    centroids[i] = x[i]

for i in range(max_iterations):
    clusters = {}

    for j in range(cluster_num):
        clusters[j]=[]

    for location in x:
        distances = []
        for centroid_no in centroids:
            distances += [np.linalg.norm(location-centroids[centroid_no])]
        #distances = [np.linalg.norm(location - centroids[centroid_no]) for centroid_no in centroids]
        clus_num = distances.index( min(distances) )
        clusters[clus_num].append(location)
    
    prev_centroids = dict(centroids)
    for cluster_no in clusters:
        centroids[cluster_no] = np.average(clusters[cluster_no],axis=0)

    isOptimal = True

    for centroid_no in centroids:
        ori_centroid = prev_centroids[centroid_no]
        new_centroid = centroids[centroid_no]

        if np.sum((ori_centroid-new_centroid)/ori_centroid*100)>tolerance:
            isOptimal=False

        
    if isOptimal:
        break


#print(centroids)
artists=[]
for cluster_no in clusters:
    color = colors[cluster_no]
    cluster_name = cluster_names[cluster_no]
    x=y=[]
    for location in clusters[cluster_no]:
        artist = plt.scatter(x=location[0],y=location[1],label=cluster_name,color=color,s=30)
    artists.append(artist)
    # Here, artist is taken because we need the color of the last point mapped in the cluster
    # And Artists is the list of such artist of each cluster

for centroid_no in centroids:
    plt.scatter(centroids[centroid_no][0],centroids[centroid_no][1],label="Centroid of "+cluster_names[centroid_no],color=colors[centroid_no],s=130,marker='x')

plt.xlabel("East Direction")
plt.ylabel("North Direction")
plt.title("Shop Plotting")
plt.legend(artists,cluster_names[:cluster_num])
plt.show()

print("The number of shops needed are:",cluster_num)