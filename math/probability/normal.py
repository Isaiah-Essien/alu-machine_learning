#!/usr/bin/env python3

'''Module for calculating normal distribution'''


class Normal:
    """
    Represents a normal distribution.

    Attributes:
        mean (float): The mean of the distribution.
        stddev (float): The standard deviation of the distribution.
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initializes the Normal distribution with data or given mean and stddev.

        Args:
            data: List of the data to be used to estimate the distribution.
            mean: The mean of the distribution.
            stddev: The standard deviation of the distribution.

        Raises:
            ValueError: If stddev is not a positive value.
            TypeError: If data is not a list.
            ValueError: If data does not contain multiple values.
        """
        if stddev <= 0:
            raise ValueError('stddev must be a positive value')
        if data is None:
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = float(sum(data) / len(data))
            self.stddev = float(
                (sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value.

        Args:
            x: The x-value.

        Returns:
            float: The z-score of x.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score.

        Args:
            z: The z-score.

        Returns:
            float: The x-value of z.
        """
        return self.mean + z * self.stddev
