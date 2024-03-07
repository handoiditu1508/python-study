import numpy as np

B = np.arange(3)
B  # array([0, 1, 2])

np.exp(B)  # array([1.        , 2.71828183, 7.3890561 ])
np.sqrt(B)  # array([0.        , 1.        , 1.41421356])

C = np.array([2.0, -1.0, 4.0])
np.add(B, C)  # array([2., 0., 6.]
