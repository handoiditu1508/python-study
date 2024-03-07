import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
b  # array([0, 1, 2, 3])

c = a - b
c  # array([20, 29, 38, 47])

b**2  # array([0, 1, 4, 9])

10 * np.sin(a)  # array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])

a < 35  # array([ True,  True, False, False])

# matrix dot product
A = np.array(
    [
        [1, 1],
        [0, 1],
    ]
)
B = np.array(
    [
        [2, 0],
        [3, 4],
    ]
)

# elementwise product
A * B
# array([[2, 0],
#        [0, 4]])

# matrix product
A @ B
# array([[5, 4],
#        [3, 4]])

# another matrix product
A.dot(B)
# array([[5, 4],
#        [3, 4]])

# modify existing array
rg = np.random.default_rng(1)  # create instance of default random number generator
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
a
# array([[3, 3, 3],
#        [3, 3, 3]])

b += a
b
# array([[3.51182162, 3.9504637 , 3.14415961],
#        [3.94864945, 3.31183145, 3.42332645]])

# a += b  # error b is not automatically converted to integer type

# unary operations
rg = np.random.default_rng(1)  # create instance of default random number generator
a = rg.random((2, 3))
a
# array([[0.51182162, 0.9504637 , 0.14415961],
#        [0.94864945, 0.31183145, 0.42332645]])
a.sum()  # 3.290252281866131
a.min()  # 0.14415961271963373
a.max()  # 0.9504636963259353

# unary on specific axis
b = np.arange(12).reshape(3, 4)
b
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

# sum of each column
b.sum(axis=0)  # array([12, 15, 18, 21])

# min of each row
b.min(axis=1)  # array([0, 4, 8])

# cumulative sum along each row
b.cumsum(axis=1)
# array([[ 0,  1,  3,  6],
#        [ 4,  9, 15, 22],
#        [ 8, 17, 27, 38]])
