#!/usr/bin/env python3

'''This script finads the mean of a covariance '''


import numpy as np


def mean_cov(X):
    """
    Calculates the mean and covariance of a data set.

    Parameters:
    X (numpy.ndarray): A 2D array of shape (n, d) containing the data set
        n (int): The number of data points
        d (int): The number of dimensions in each data point

    Returns:
    mean (numpy.ndarray): A 1D array of shape (1, d)
    cov (numpy.ndarray): A 2D array of shape (d, d)

    Raises:
    TypeError: If X is not a 2D numpy.ndarray
    ValueError: If n is less than 2
    """

    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape

    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate the mean of the data set
    mean = np.mean(X, axis=0).reshape(1, d)

    # Center the data by subtracting the mean
    X_centered = X - mean

    # Calculate the covariance matrix
    cov = np.dot(X_centered.T, X_centered) / (n - 1)

    return mean, cov


def correlation(C):
    """
    Calculates the correlation matrix from a covariance matrix.
    
    Parameters:
    C (numpy.ndarray): A 2D array of shape (d, d) containing the covariance matrix
        d (int): The number of dimensions
    
    Returns:
    numpy.ndarray: A 2D array of shape (d, d) containing the correlation matrix
    
    Raises:
    TypeError: If C is not a numpy.ndarray
    ValueError: If C does not have shape (d, d)
    """

    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    d = C.shape[0]

    # Calculate the standard deviations
    std_devs = np.sqrt(np.diag(C))

    # Create the correlation matrix
    correlation_matrix = np.zeros((d, d))

    for i in range(d):
        for j in range(d):
            correlation_matrix[i, j] = C[i, j] / (std_devs[i] * std_devs[j])

    return correlation_matrix
