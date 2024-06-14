#!/usr/bin/env python3

'''This scripts computes a Multiverse distribution'''


import numpy as np


class MultiNormal:
    """
    Represents a Multivariate Normal distribution.
    """

    def __init__(self, data):
        """
        Class constructor.

        Parameters:
        data (numpy.ndarray): A 2D array of shape (d, n)
            n (int): The number of data points
            d (int): The number of dimensions in each data point

        Raises:
        TypeError: If data is not a 2D numpy.ndarray
        ValueError: If n is less than 2
        """
        if not isinstance(data, np.ndarray) or len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Calculate the mean of the data set
        self.mean = np.mean(data, axis=1).reshape(d, 1)

        # Center the data by subtracting the mean
        data_centered = data - self.mean

        # Calculate the covariance matrix
        self.cov = np.dot(data_centered, data_centered.T) / (n - 1)
