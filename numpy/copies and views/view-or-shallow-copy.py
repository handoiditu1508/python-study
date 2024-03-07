import numpy as np

a = np.array(
    [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
    ]
)

c = a.view()
c is a  # False
c.base is a  # True
c.flags.owndata  # False

c = c.reshape((2, 6))  # a's shape doesn't change
a.shape  # (3,4)

c[0, 4] = 1234  # a's data changes
a
# array([[   0,    1,    2,    3],
#        [1234,    5,    6,    7],
#        [   8,    9,   10,   11]])


# Slicing an array returns a view of it
s = a[:, 1:3]
s[:] = 10  # s[:] is a view of s
a
# array([[   0,   10,   10,    3],
#        [1234,   10,   10,    7],
#        [   8,   10,   10,   11]])
