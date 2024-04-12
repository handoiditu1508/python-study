import numpy as np

a = np.arange(12).reshape(3, 4)
a
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

b = a > 4
b
# array([[False, False, False, False],
#        [False,  True,  True,  True],
#        [ True,  True,  True,  True]])

a[b]  # 1d array with the selected elements
# array([ 5,  6,  7,  8,  9, 10, 11])

a[b] = 0  # All elements of `a` higher than 4 become 0
a
# array([[0, 1, 2, 3],
#        [4, 0, 0, 0],
#        [0, 0, 0, 0]])


# The second way of indexing with booleans
a = np.arange(12).reshape(3, 4)
a
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
b1 = np.array([False, True, True])  # first dim selection
b2 = np.array([True, False, True, False])  # second dim selection

a[b1, :]
# array([[ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

a[b1]
# array([[ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

a[:, b2]
# array([[ 0,  2],
#        [ 4,  6],
#        [ 8, 10]])

# pairs the first True in b1 with the first True in b2 (1, 0)
# pairs the second True in b1 with the second True in b2 (2, 2)
a[b1, b2]
# array([ 4, 10])
