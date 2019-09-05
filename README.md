# Machine Learning Workshop Series

## Day 5 Contents

* Day 5:
  * Supervised Learning
  * Introduction to Regression
  * Linear regression
  * Naive bayes classifier
  * Decision trees
  * Wrap up and look up the different supervised learning algorithms

## Summary

* Spervised learning consists of:
  * Regression      (Calculate particular values)
  * Classification  (Seperate into individual classes)

* We'll cover the basic explanation of some widely used algorithms and provide some of the python codes for you to practise.

## Content

### Regression

* Regression is basically, predicting the particular value of the data at that point
* For e.g. Predicting the prices of silver, based upon the data of last 25 years.
* Here, the price of silver will be a real valued value which can be a range, but not a class.

### Classification

* As previouslty noted:
  * Classification is basically predicting the group of the given data.
  * As an Example, To separate people into male and female according to their BMI stats.
  * Here we make groups based on some previously known data and predict the group/class of the predicting data.

### Methods of Regression

* The widely known methods for regression are:
  * Linear Regression
  * Logistic Regression
  * Polynomial Regression
  * Stepwise Regression
  * Ridge Regression
  * Lasso Regression
  * ElasticNet Regression

### Methods of Classification

* The widely known methods for classification are:
  * Logistic Regression
  * Naive-Bayes Classifier
  * K Nearest Neighbors (KNN)
  * Supprt vector machine (SVM)
  * Decision trees
  * Random forest
  * Neural Networks

### Linear Regression

* Wiki: [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)
* Here, we train our model to learn the slope(variable m) and shift(constant c) from the provided data.
* A clear explanation about linear regression and it's types are provided at:[Machine Learning Mastery](https://machinelearningmastery.com/linear-regression-for-machine-learning/)
* An example of linear regression and it's implemented code with a custom dataset is provided at : [Towards Data Science](https://towardsdatascience.com/linear-regression-detailed-view-ea73175f6e86)

### Polynomial Regression

* Polynomial regression is the same as linear regression with the curve changed from line to a polynomial curve.
* A clear explanation about Polynomial regression with Boston Housing dataset in python is provided at : [Towards Data Science](https://towardsdatascience.com/polynomial-regression-bbe8b9d97491)

### Naive Bayes classifier

* Naive bayes classifier is a classification technique based upon probabilities of different features we input. It calculates the probability of the test data based upon the relation of occurences in the training dataset by using bayes theorem.
* Wiki : [Naive Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
* A simple and concise explanation along with code is given at : [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2017/09/naive-bayes-explained/?#)

### Logistic Regression

* Even though the name suggests it to be a regression method, it can also be considered as a classification method.
* Wiki: [Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression)
* Logistic regression is used for situations where there are only 2 outcomes(Dichotomy). It is similar to linear regression by replacing the linear curve(line) with an S-shaped curve called logistic function.
* A detailed explanation of logistic regression along with the code is beautifully presented at :[Towards Data Science](https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc) by [Saishruthi Swaminathan](https://towardsdatascience.com/@saishruthi.tn)

### Decision trees

* Decision trees are basically binary trees which have nodes as decision questions and branches are in accordance to decisions.
* Wiki: [Decision Tree](https://en.wikipedia.org/wiki/Decision_tree)
* A better and thorough explanation is given at:[Towards Data Science](https://towardsdatascience.com/decision-trees-in-machine-learning-641b9c4e8052) and (explanation + code) is given at :[Medium Article by Rajesh S. Brid](https://medium.com/greyatom/decision-trees-a-simple-way-to-visualize-a-decision-dc506a403aeb)

### Neural Network

* Neural Network is a set of methods of supervised learning that mimics the way a human brain operates.
* Wiki: [Neural Network](https://en.wikipedia.org/wiki/Artificial_neural_network)
* These methods are most commonly known as deep learning, synonymous to the deep architecture of neurons in a human brain.
* We'll cover this topic under [Day 6](https://github.com/TechNeurons/ML-Workshop/tree/Day-6)

### Try-It-Yourself

* Try Day 4 [Try-it-Yourself](https://github.com/TechNeurons/ML-Workshop/blob/Day-4/Try-it-Yourself/Try_it_yourself.md) using Naive-bayes classifier.

* Well, look up the other techniques of supervised learning like SVM and Random forest. We'll continue with others and go in detail about some methods in the future in advanced ML Series. Stay Tuned! :)
