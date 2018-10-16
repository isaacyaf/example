# Readme
These files (or codes) are used for illustration and education purposes.

* [Logic Gate Simulation](#logic-gate-simulation)
* [MNIST by Keras](#mnist-by-keras)
* [The Custom Loss Function of Keras](#the-custom-loss-function-of-Keras)
* [Titanic Survival Prediction](#titanic-survival-prediction)
***

## Logic Gate Simulation
The result is done by a neural network(without DL framework).
<p>
[The code](https://github.com/isaacyaf/example/blob/master/SampleNeuralNetwork_Logic_Gate_Simulation.ipynb)

How should I choose the analysis method?
<p>

[examples]: https://github.com/isaacyaf/example/blob/master/images/examples_ofMethods.PNG

<p>
    These three examples analyze logic gates with neural networks, selection trees (rules), and simple descriptive statistics.
<p>
Q: 
<p>
        
**Can we use any kind of mechanical learning method to simulate a logic gate(or something else)?**
        
<p>
A: 
<p>
    
    Of course, we can learn the logic gate results repeatedly with a difficult method just like deep learning.
<p>
    But if the problem is not difficult (the rules can explain) or we know enough about the problem, we can consider other methods (for example: Decision tree)
<p>
    Even more we can observe some phenomena with descriptive statistics. When any of our inputs is equal to 0, our output is equal to 1 with a 0% probability.


***

## MNIST by Keras
Keras examples
This contains two examples: 
* MNIST
* Fashion MNIST

***

## The Custom Loss Function of Keras
The two loss function codes are actually applied to the internal framework.
* mean_absolute_percentage_error
* mean_squared_error
<p>
I put the code in the custom "def function" and show the calling process(mean_squared_error) with MNIST.

***

## Titanic Survival Prediction
The training data has been pre-processed. 
This example lets you pick some features and build a simple DNN model to predict survival.
<p>
Features Preview:
    
|Col. Name      | Data Explanation  |
|:----------    |:---------------   |
|PassengerId    ||   
|Pclass         |1/2/3              |
|Name           ||
|Name_length    ||
|Title          | 1: Mr <br> 2: Miss   <br> 3: Mrs <br> 4: Master  <br> 5: Rare <br><br> Rare = 'Capt', 'Col', 'Countess', 'Don', 'Dr',<br> 'Jonkheer', 'Lady', 'Major', 'Rev', 'Sir'|
|Sex            |0: Female <br> 1: Male|
|Age            ||
|Age_Categories |0: ≤ 16 <br> 1: > 16 &  ≤ 32  <br> 2: > 32 &  ≤ 48  <br> 3: > 48 & ≤ 64  <br> 4: > 64 |
|SibSp          ||
|Parch          ||
|FamilySize     |SibSp + Parch + 1|
|IsAlone        |0: No <br> 1: Yes|
|Ticket         ||
|Fare           ||
|Fare_Categories|0: ≤ 7.91 <br> 1: > 7.91 &  ≤ 14.454  <br> 2: > 14.454 &  ≤ 31  <br> 3: > 31  |
|Cabin          ||
|Has_Cabin      |0: No <br> 1: Yes|
|Embarked       |0 = Southampton <br> 1 = Cherbourg  <br> 2 = Queenstown  |
|Survived       |0 = No, 1 =Yes|
 
<p>
I have prepared two subsets and used to show the results.

*   Group 1:

    > Duane, Mr. Frank
    > Svensson, Mr. Johan
    > Turkula, Mrs. (Hedwig)
    > Herman, Miss. Alice
    > Braund, Mr. Owen Harris

*   Group 2:

    > Guggenheim, Mr. Benjamin
    > Byles, Rev. Thomas Roussel Davids
    > Rosalie Ida Blun
    > Lines, Miss. Mary Conover
    > Blank, Mr. Henry



***
