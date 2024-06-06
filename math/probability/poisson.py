#!/usr/bin/env python3
class Poisson:
    '''
    This class calculates the function of a lambtha checking if the data is greater than 2,
    and if lambtha is greater than 0
    '''
    def __init__(self, data=None, lambtha=1.):
        # Validate lambtha
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        
        # Handle case when data is None (not provided)
        if data is None:
            self.lambtha = float(lambtha)
        else:
            # Validate data
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate lambtha from data
            self.lambtha = float(sum(data) / len(data))

# Example usage
if __name__ == "__main__":
    import numpy as np

    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()

    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
