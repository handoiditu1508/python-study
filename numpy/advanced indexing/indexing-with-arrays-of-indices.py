import numpy as np

a = np.arange(12) ** 2  # the first 12 square numbers
i = np.array([1, 1, 3, 8, 5])  # an array of indices
a[i]  # the elements of `a` at the positions `i`
# array([ 1,  1,  9, 64, 25])

j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
a[j]  # the same shape as `j`
# array([[ 9, 16],
#        [81, 49]])


# When the indexed array a is multidimensional, a single array of indices refers to the first dimension of a
palette = np.array(
    [
        [0, 0, 0],  # black
        [255, 0, 0],  # red
        [0, 255, 0],  # green
        [0, 0, 255],  # blue
        [255, 255, 255],  # white
    ]
)
image = np.array(
    [
        [0, 1, 2, 0],
        [0, 3, 4, 0],
    ]  # each value corresponds to a color in the palette
)
palette[image]  # the (2, 4, 3) color image
# array([[[  0,   0,   0],
#         [255,   0,   0],
#         [  0, 255,   0],
#         [  0,   0,   0]],

#        [[  0,   0,   0],
#         [  0,   0, 255],
#         [255, 255, 255],
#         [  0,   0,   0]]])


# give indexes for more than one dimension
a = np.arange(12).reshape(3, 4)
a
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
i = np.array(
    [
        [0, 1],  # indices for the first dim of `a`
        [1, 2],
    ]
)
j = np.array(
    [
        [2, 1],  # indices for the second dim
        [3, 3],
    ]
)
a[i, j]  # i and j must have equal shape
# array([[ 2,  5],
#        [ 7, 11]])

a[i, 2]
# array([[ 2,  6],
#        [ 6, 10]])

a[:, j].shape  # (3, 2, 2)
a[:, j]
# array([[[ 2,  1],
#         [ 3,  3]],

#        [[ 6,  5],
#         [ 7,  7]],

#        [[10,  9],
#         [11, 11]]])


# index with tuple
# equivalent to a[i, j]
a[(i, j)]
# array([[ 2,  5],
#        [ 7, 11]])
