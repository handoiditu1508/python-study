import numpy as np

a = np.array(
    [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
    ]
)
b = a  # no new object is created
b is a  # True


# Python passes mutable objects as references, so function calls make no copy
def f(x):
    print(id(x))


id(a)  # 2378003675344
f(a)  # 2378003675344
