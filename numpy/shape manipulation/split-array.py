import numpy as np

a = np.arange(24).reshape(2, 12)
a
# array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11],
#        [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]])

# Split `a` into 3
np.hsplit(a, 3)
# [array([[ 0,  1,  2,  3],
#         [12, 13, 14, 15]]),
#  array([[ 4,  5,  6,  7],
#         [16, 17, 18, 19]]),
#  array([[ 8,  9, 10, 11],
#         [20, 21, 22, 23]])]

# Split `a` after the third and the fourth column
np.hsplit(a, (3, 4))
# [array([[ 0,  1,  2],
#         [12, 13, 14]]),
#  array([[ 3],
#         [15]]),
#  array([[ 4,  5,  6,  7,  8,  9, 10, 11],
#         [16, 17, 18, 19, 20, 21, 22, 23]])]
