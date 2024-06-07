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
            q = 1 - p
            variance = sum((x - p) ** 2 for x in data) / len(data)
            n = int(round(p * q / variance))
            p = sum(data) / n
            self.n = n
            self.p = p

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given k-value.

        Args:
            k: The k-value.

        Returns:
            float: The PMF value for k.
        """
        return (self.factorial(self.n) / (self.factorial(k) * self.factorial(self.n - k))) * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given k-value.

        Args:
            k: The k-value.

        Returns:
            float: The CDF value for k.
        """
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf

    def factorial(self, n):
        """
        Calculates the factorial of a given integer.

        Args:
            n: The integer.

        Returns:
            int: The factorial of n.
        """
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
