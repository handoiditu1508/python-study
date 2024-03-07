import numpy as np

# 1D arrays
z = np.array([1, 2])
x = np.array([3, 4])
np.row_stack((z, x))
# array([[1, 2],
#        [3, 4]])
np.column_stack((z, x))
# array([[1, 3],
#        [2, 4]])
np.vstack((z, x))
# array([[1, 2],
#        [3, 4]])
np.hstack((z, x))
# array([1, 2, 3, 4])

# View as 2D column vector
z[:, np.newaxis]
# array([[1],
#        [2]])
x[:, np.newaxis]
# array([[3],
#        [4]])
np.column_stack((z[:, np.newaxis], x[:, np.newaxis]))
# array([[1, 3],
#        [2, 4]])
np.hstack((z[:, np.newaxis], x[:, np.newaxis]))
# array([[1, 3],
#        [2, 4]])

# 2D arrays
z = np.array(
    [
        [1, 2],
        [3, 4],
    ]
)
x = np.array(
    [
        [5, 6],
        [7, 8],
    ]
)
np.row_stack((z, x))
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
np.column_stack((z, x))
# array([[1, 2, 5, 6],
#        [3, 4, 7, 8]])
np.vstack((z, x))
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
np.hstack((z, x))
# array([[1, 2, 5, 6],
#        [3, 4, 7, 8]])

np.column_stack is np.hstack  # False
np.row_stack is np.vstack  # True

# creating arrays by stacking numbers along one axis
np.r_[1:4, 0, 4]  # array([1, 2, 3, 0, 4])
np.c_[np.array([[1, 2, 3]]), 0, 0]  # array([[1, 2, 3, 0, 0]])
