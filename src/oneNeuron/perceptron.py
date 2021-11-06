import os
import joblib
import numpy as np
import pandas as pd


class Perceptron:
    """
       creating a Perceptron class
    """
    def __init__(self,eta,epochs):
        self.weights    =   np.random.randn(3)
        print(f"initial weights before training: \n{self.weights}")
        self.eta        =   eta
        self.epochs     =   epochs

    def activationFunction(self, inputs, weights):
        """[summary]
        Args:
            inputs ([data]): input data
            weights ([int]): adding some extra data
        Returns:
            [numpy array]: returning into numpy array
        """
        z              =    np.dot(inputs, weights) #  z = w*x
        return np.where(z > 0,1,0)#condition if true false

    def fit(self, X, y):
        """fitting the data
        Args:
            X ([df]): independent variable
            y ([df]): dependent variable
        """
        self.X    =  X 
        self.y    =  y

        X_with_bias = np.c_[self.X, -np.ones((len(self.X),1))]
        print(f"X with bias: \n{X_with_bias}")

        for epoch in range(self.epochs):
            print("----"*10)
            print(f"for epoch: {epoch}")
            print("___"*10)

            y_hat = self.activationFunction(X_with_bias, self.weights)# forward propogation
            print(f"predicted value after forward pass: \n{y_hat}")
            self.error = self.y - y_hat
            print(f"error: \n{self.error}")
            self.weights = self.weights + self.eta * np.dot(X_with_bias.T, self.error)#backward propogation
            print(f"updated weight after epoch: \n{epoch}/{self.epochs} : \n{self.weights}")
            print("###"*10)

    def predict(self,X):
        """
           predicting the value 
        """
        X_with_bias = np.c_[X, -np.ones((len(X), 1))]
        return self.activationFunction(X_with_bias,self.weights)

    def total_loss(self):
        """ calculating the loss of trained model
        """
        total_loss = np.sum(self.error)
        print(f"total loss: {total_loss}")
        return total_loss         