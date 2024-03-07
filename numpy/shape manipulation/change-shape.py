import numpy as np

rg = np.random.default_rng(1)  # create instance of default random number generator

a = np.floor(10 * rg.random((3, 4)))
a
# array([[5., 9., 1., 9.],
#        [3., 4., 8., 4.],
#        [5., 0., 7., 5.]])
a.shape
# (3, 4)

# returns the array, flattened
a.ravel()  # array([5., 9., 1., 9., 3., 4., 8., 4., 5., 0., 7., 5.])

# returns the array with a modified shape
a.reshape(6, 2)
# array([[5., 9.],
#        [1., 9.],
#        [3., 4.],
#        [8., 4.],
#        [5., 0.],
#        [7., 5.]])

# returns the array, transposed
a.T
# array([[5., 3., 5.],
#        [9., 4., 0.],
#        [1., 8., 7.],
#        [9., 4., 5.]])
a.T.shape  # (4, 3)

# like reshape but modify the array
a.resize(2, 6)
a
# array([[5., 9., 1., 9., 3., 4.],
#        [8., 4., 5., 0., 7., 5.]])

# If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated
a.reshape(3, -1)
# array([[5., 9., 1., 9.],
#        [3., 4., 8., 4.],
#        [5., 0., 7., 5.]])
