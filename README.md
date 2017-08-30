# Why I forked?

The goal of forking from <https://github.com/MichalDanielDobrzanski/DeepLearningPython35> was to do the last exercise in [chapter 2](http://neuralnetworksanddeeplearning.com/chap2.html) of [neuralnetworksanddeeplearning.com](neuralnetworksanddeeplearning.com "Neural Networks and Deep Learning by Michael Nielsen") where the author asks to *"Modify network.py so that it uses this fully matrix-based approach"*. The result is in **network_mat.py**. I changed only the `update_mini_batch` function of original **network.py**.

The **test_mat.py** is for comparing the performances of **network.py** and **network_mat.py**.

# Aditional modifications
## L1 regularization and Momentum-based gradient descent
Modified network2.py to be able to use L1 regularization (see problem [here](http://neuralnetworksanddeeplearning.com/chap3.html#problems_201277)) and momentum-based stochastic gradient descent (see problem [here](http://neuralnetworksanddeeplearning.com/chap3.html#problem_713937)).

# Content of original README.md
## Overview

### neuralnetworksanddeeplearning.com integrated scripts for Python 3.5.2 and Theano with CUDA support

These scrips are updated ones from the **neuralnetworksanddeeplearning.com** gitHub repository in order to work with Python 3.5.2

The testing file (**test.py**) contains all three networks (network.py, network2.py, network3.py) from the book and it is the starting point to run (i.e. *train and evaluate*) them.

## Just type at shell: **python3.5 test.py**

In test.py there are examples of networks configurations with proper comments. I did that to relate with particular chapters from the book.


