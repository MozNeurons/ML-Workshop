# Machine Learning Workshop Series

## Day 3 Contents

* Day 3 :
  * Unsupervised Learning
  * Introduction to clustering
  * Types of clustering
  * Methods of Clustering
  * K-Means clustering
  * Differences between different types of clustering

## Summary

* Unspervised learning consists of:
  * Clustering (Cluster Analysis)
  * Principal component analysis

### Clustering

* Clustering can be related to 'Grouping'
* Reference : [NPTEL PPT](https://github.com/MozNeurons/ML-Workshop/blob/Day-3/9A-clustering-intro.pptx)
* Here we group data together based on some model
* The widely-known approaches to clustering are:
  * Partitioning: Construct various partitions and then evaluate them by some criterion. (Popular Methods: K-Means)
  * Hierarchical: Create a hierarchical decomposition of the set of objects using some criterion.
  * Model-based: Hypothesize a model for each cluster and find best fit of models to data.
  * Density-based: Guided by connectivity and density functions. (Popular Methods: DBSCAN , OPTICS)
  * Graph-Theoretic Clustering.

* Looking up Partition clustering, We move onto the widely known clustering algorithm known as K-means Algorithm

### K-MEANS CLUSTERING

* K-means algorithm is an algorithm based on Centroid model of clustering.

* References: [NPTEL PPT](https://github.com/MozNeurons/ML-Workshop/blob/Day-3/9B-kmeans-clustering.pptx) / [PPT by Jing Gao](https://github.com/MozNeurons/ML-Workshop/blob/Day-3/clustering_partitional.pdf)

* Algorithm:
  * Given k
  1. Randomly choose k data points (seeds) to be the initial cluster centres.
  2. Assign each data point to the closest cluster centre.
  3. Re-compute the cluster centres using the current cluster memberships.
  4. If a convergence criterion is not met, go to 2.

* Here, to choose the closest cluster, i.e. to calculate the distance, our program uses Euclidean distance form ula. Variant of it has Manhattan or cosine distance formula.

* The example approach we take to introduce clustering is:
  * Consider a Pizza franchise who wants to open Outlets in a city. Given the population distribution, Find out the min. number of frachise it needs to open depending upon the population.
  * The dataset of the population distribution is given in : [Distribution-1](https://github.com/MozNeurons/ML-Workshop/blob/Day-3/Datasets/Distribution-1.csv)

* The solved K-means algorithm code is given in : [https://github.com/MozNeurons/ML-Workshop/blob/Day-3/K-means.py]

* The question is also solved with a Python library called Scikit-learn. You can have a look at the code at :[https://github.com/MozNeurons/ML-Workshop/blob/Day-3/K-Means_by_Library.py]

* The comparison of different clustering algorithms provided by scikit-learn is also in the docs (Note: Update scikit-learn to the latest version after 21.1 as versions 20.x didn't have the OPTICS algorithm): [https://github.com/MozNeurons/ML-Workshop/blob/Day-3/plot_cluster_comparison.py]

* Enjoy Learning :)

## TRY-IT-YOURSELF

* After looking up our resources and learning, try these questions to get a better grasp on the clustering techniques : [Try it Yourself](https://github.com/MozNeurons/ML-Workshop/blob/Day-3/Try-It-Yourself/Try_it_yourself.md)

## References

* NPTEL course : [Introduction to machine learning by Prof. Sudheshna Sarkar](https://nptel.ac.in/courses/106105152/)

* [Scikit-learn](https://scikit-learn.org/stable/)

* Datasets : [K-means properties on six clustering benchmark datasets by P. Fränti and S. Sieranoja](http://cs.joensuu.fi/sipu/datasets/)
