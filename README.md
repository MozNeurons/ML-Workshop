# Machine Learning Workshop Series

## Day 3 Contents

* Day 3 :
  * Theory: (Look and read these topics before jumping on the hands-on)
    * Intro to Neural networks
    * Perceptron and it's relation with neurons
    * Single layer Perceptron models
    * Activation functions
    * Multi-layer perceptrons
    * Front and back propagation.
  * Practical (Hands On):
    * Aritficial Neural Network with 3 layers using keras

## Summary

* Neural Networks(NNs) make up a section of Machine learning known as deep learning
* These neural networks are designed upon the human nervous system/network.
* Generally these NNs mostly apply supervised learning. i.e. they need to be trained before prediction.
* The simple ANN we will construct is also a supervised learning technique.
* The [Data.md](https://github.com/TechNeurons/ML-Workshop/blob/Day-6/Data.md) file contains important links to some of the resources.

### Neural Networks

* Wiki: [Artificial Neural Network](https://en.wikipedia.org/wiki/Artificial_neural_network) or [Neural Network](https://en.wikipedia.org/wiki/Neural_network)

* A nice explanation about deep learning is provided at: [Machine Learning mastery article by Jason Brownlee](https://machinelearningmastery.com/what-is-deep-learning/)
* A nice explanation of deep learning + Neural networks with more references is provided in the presentation : [deep-learning.pptx](http://times.cs.uiuc.edu/course/510f17/ppt/deep-learning.pptx)

* [Keras](https://keras.io/) is a Neural network library written in python. It runs upon tensorflow, micorsoft cognitive toolkit, theano or plaidML.
* For our example, we use [keras](https://keras.io/) to implement neural network and make our machine learn.
* Our example, we use the Churn modelling example. For which the dataset is available at : [Kaggle](https://www.kaggle.com/shrutimechlearn/churn-modelling) or in the repo: [Dataset](https://github.com/TechNeurons/ML-Workshop/blob/Day-6/Churn_Modelling.csv).

### Artificial neural Network

* We recommend to run the following example on [Colab by Google](https://colab.research.google.com) because of the Keras and Hardware dependencies in every architecture.

* The example can be viewed at: [ANN example.ipynb](https://colab.research.google.com)

* Method:
  * Neural networks contain Layers of multiple perceptrons(Virtual Neurons).
  * Each perceptron has its own activation function
  * Each perceptron can have multiple inputs as well as one or more outputs.
  * A network is trained by iteratively setting the weights by providing the same input data using front or back propagation. These iterations are called epoch.
  * Due to the concept of the [Dying RELU](https://www.tinymind.com/learn/terms/relu#dying-relu), we need to initialize the weights closer to zero but not zero. Hence, we preprocess the data using StandardScalar from scikit-learn preprocessing library.

* We have taken our example from an article on : [Towards Data Science by Siddhart Dixit](https://towardsdatascience.com/building-your-own-artificial-neural-network-from-scratch-on-churn-modeling-dataset-using-keras-in-690782f7d051)

* Enjoy Learning :)

## TRY-IT-YOURSELF

* After looking up our resources and learning, try these questions to get a better grasp on the concepts and go-arounds: [Try it Yourself](https://github.com/TechNeurons/ML-Workshop/blob/Day-6/Try-It-Yourself/Try_it_yourself.md)
