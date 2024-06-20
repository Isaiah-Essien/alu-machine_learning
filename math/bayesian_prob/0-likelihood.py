#!/usr/bin/env python3

'''Script'''

import numpy as np


def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient "n choose k".

    Parameters:
    n (int): Total number of items.
    k (int): Number of items to choose.

    Returns:
    int: Binomial coefficient.
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def likelihood(x, n, P):
    """
    Calculates the likelihood of observing the data,
    given various hypothetical probabilities.

    Parameters:
    x (int): Number of patients with severe side effects.
    n (int): Total number of patients.
    P (numpy.ndarray): Array of hypothetical probabilities.

    Returns:
    numpy.ndarray: Likelihoods for each probability in P.

    Raises:
    ValueError: If n or x is invalid, or if any value in P is out of range.
    TypeError: If P is not a 1D numpy.ndarray.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        raise ValueError(
            "x must be an integer that is greater than or equal to 0")

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if np.any((P < 0) | (P > 1)):
        raise ValueError("All values in P must be in the range [0, 1]")

    coeff = binomial_coefficient(n, x)
    likelihoods = coeff * (P ** x) * ((1 - P) ** (n - x))

    return likelihoods
