#!/usr/bin/env python3

'''Binomial here and there '''


class Binomial:
    """
    Represents a binomial distribution.

    Attributes:
        n (int): The number of Bernoulli trials.
        p (float): The probability of a "success".
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initializes the Binomial distribution with data or given n and p.

        Args:
            data: List of the data to be used to estimate the distribution.
            n: The number of Bernoulli trials.
            p: The probability of a "success".

        Raises:
            ValueError: If n is not a positive value or p is not a valid probability.
            TypeError: If data is not a list.
            ValueError: If data does not contain multiple values.
        """
        if n <= 0:
            raise ValueError("n must be a positive value")
        if p <= 0 or p >= 1:
            raise ValueError("p must be greater than 0 and less than 1")

        if data is None:
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            p = sum(data) / len(data)
            n = round(sum(data) / p)
            p = sum(data) / n
            self.n = int(n)
            self.p = float(p)
