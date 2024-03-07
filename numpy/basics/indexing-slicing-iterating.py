import numpy as np

# One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python sequences
a = np.arange(10) ** 3
a  # array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
a[2]  # 8
a[2:5]  # array([ 8, 27, 64])

# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000
a[:6:2] = 1000
a  # array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])

# reverse a
a[::-1]  # array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])

for i in a:
    print(i ** (1 / 3.0))
# 9.999999999999998
# 1.0
# 9.999999999999998
# 3.0
# 9.999999999999998
# 5.0
# 5.999999999999999
# 6.999999999999999
# 7.999999999999999
# 8.999999999999998

# Multidimensional arrays can have one index per axis. These indices are given in a tuple separated by commas
b = np.fromfunction(lambda x, y: 10 * x + y, (5, 4), dtype=int)
b
# array([[ 0,  1,  2,  3],
#        [10, 11, 12, 13],
#        [20, 21, 22, 23],
#        [30, 31, 32, 33],
#        [40, 41, 42, 43]])
b[2, 3]  # 23

# each row in the second column of b
# equivalent to b[:, 1]
b[0:5, 1]  # array([ 1, 11, 21, 31, 41])

# each column in the second and third row of b
b[1:3, :]
# array([[10, 11, 12, 13],
#        [20, 21, 22, 23]])

# the last row. Equivalent to b[-1, :]
b[-1]  # array([40, 41, 42, 43])

# The dots (...) represent as many colons as needed to produce a complete indexing tuple then
# x[1, 2, ...] is equivalent to x[1, 2, :, :, :]
# x[..., 3] is equivalent to x[:, :, :, :, 3]
# x[4, ..., 5, :] is equivalent to x[4, :, :, 5, :]

# a 3D array (two stacked 2D arrays)
c = np.array(
    [
        [[0, 1, 2], [10, 12, 13]],
        [[100, 101, 102], [110, 112, 113]],
    ]
)
c.shape  # (2, 2, 3)

c[1, ...]  # same as c[1, :, :] or c[1]
# array([[100, 101, 102],
#        [110, 112, 113]])

c[..., 2]  # same as c[:, :, 2]
# array([[  2,  13],
#        [102, 113]])

# Iterating over multidimensional arrays is done with respect to the first axis
b = np.fromfunction(lambda x, y: 10 * x + y, (5, 4), dtype=int)
for row in b:
    print(row)
# [0 1 2 3]
# [10 11 12 13]
# [20 21 22 23]
# [30 31 32 33]
# [40 41 42 43]

for element in b.flat:
    print(element)
# 0
# 1
# 2
# 3
# 10
# 11
# 12
# 13
# 20
# 21
# 22
# 23
# 30
# 31
# 32
# 33
# 40
# 41
# 42
# 43
