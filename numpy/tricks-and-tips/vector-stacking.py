import numpy as np

x = np.arange(0, 10, 2)
x  # array([0, 2, 4, 6, 8])

y = np.arange(5)
y  # array([0, 1, 2, 3, 4])

m = np.vstack([x, y])
m
# array([[0, 2, 4, 6, 8],
#        [0, 1, 2, 3, 4]])

xy = np.hstack([x, y])
xy  # array([0, 2, 4, 6, 8, 0, 1, 2, 3, 4])
