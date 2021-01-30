# Machine Learning Workshop Series

## Day 4 Contents

* Day 4 :
  * Supervised Learning
  * Introduction to classification
  * KNN Classification

## Summary

* Spervised learning consists of:
  * Regression      (Calculate particular values)
  * Classification  (Seperate into individual classes)

### Classification

* Classification is basically predicting the group of the given data.
* As an Example, To separate people into male and female according to their BMI stats.
* Here we make groups based on some previously known data and predict the group/class of the predicting data.
* There are a lot of classification techniques, based on type of approach it uses.
* Today, we'll see K Nearest-Neighbor classification (KNN Classification) which has it's similarities to K-means technique.

### K Nearest-Neighbors Classification

* By definition

  * In k-NN classification, the output is a class membership. An object is classified by a plurality vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). If k = 1, then the object is simply assigned to the class of that single nearest neighbor.

  * k-NN is a type of instance-based learning, or lazy learning, where the function is only approximated locally and all computation is deferred until classification.

* Simply putting, in KNN classification, we look up the K Nearest(Distance wise) Neighbors of the point whose class we want to predict. and depending upon the majority of the classes of it's neighbors, the point is included in that class / given it's membership.

* Algorithm:
  * Let m be the number of training data samples. Let p be an unknown point.

    1. Store the training samples in an array of data points arr[]. This means each element of this array represents a tuple (x, y).
    2. for i=0 to m:
        * Calculate Euclidean distance d(arr[i], p).
    3. Make set S of K smallest distances obtained. Each of these distances corresponds to an already classified data point.
    4. Return the majority label among S.

* To do this, we use the iris dataset, one of the standard datasets of Scikit-learn library.

* Presenting a brief about the iris dataset, Iris is a plant. i.e., according to [Wikipedia](https://en.wikipedia.org/wiki/Iris_(plant)): Iris is a genus of 260–300 species of flowering plants with showy flowers.

* The dataset consists of length and width of [sepals](https://en.wikipedia.org/wiki/Sepal) and length and width of [petals](https://en.wikipedia.org/wiki/Petal) and depending upon them, the flowers are classified accordingly into 3 categories:
  * Setosa
  * Versicolor
  * virginica

* Hence, we make our classifier classify the test data based upon the training data we provide it.

* The algorithm and design of the program is beautifully explained at : [AnalyticsVidhya](https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/)

* Look up the code : [KNN_Classifier.py](https://github.com/MozNeurons/ML-Workshop/blob/Day-4/KNN_Classifier.py) or [KNN Classification.ipynb](https://github.com/MozNeurons/ML-Workshop/blob/Day-4/KNN_Classification.ipynb)

* Scikit-learn provides a code efficient way to do classification using ti's libary function call. You can have a look at the code at : [KNN_by_Library.py](https://github.com/MozNeurons/ML-Workshop/blob/Day-4/KNN_by_Library.py) or [KNN_by_library_scikit-learn.ipynb](https://github.com/MozNeurons/ML-Workshop/blob/Day-4/KNN_by_library_scikit-learn.ipynb)

* Looking up at this classification method, We'll continue other algorithms of Supervised Learning on the next day.

### Try-It-Yourself

* Look up and try to do the [Try-it-yourself](https://github.com/MozNeurons/ML-Workshop/blob/Day-4/Try-it-Yourself/Try_it_yourself.md). [Note: You'll have to find out how to do this by online resources :) ]
