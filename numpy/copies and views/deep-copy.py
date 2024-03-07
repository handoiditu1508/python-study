import numpy as np

a = np.array(
    [
        [0, 10, 10, 3],
        [1234, 10, 10, 7],
        [8, 10, 10, 11],
    ]
)

d = a.copy()  # a new array object with new data is created
d is a  # False
d.base is a  # False
d[0, 0] = 9999
a
# array([[   0,   10,   10,    3],
#        [1234,   10,   10,    7],
#        [   8,   10,   10,   11]])


# copy should be called after slicing if the original array is not required anymore
a = np.arange(int(1e8))
b = a[:100].copy()
del a  # the memory of ``a`` can be released
# If b = a[:100] is used instead,
# a is referenced by b and will persist in memory
# even if del a is executed
