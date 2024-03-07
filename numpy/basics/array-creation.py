import numpy as np

a = np.array([2, 3, 4])
a  # array([2, 3, 4])
a.dtype  # dtype('int32')

b = np.array([1.2, 3.5, 5.1])
b.dtype  # dtype('float64')

# a = np.array(1, 2, 3, 4)  # WRONG
a = np.array([1, 2, 3, 4])  # RIGHT

# transforms sequences of sequences into two-dimensional arrays
b = np.array([(1.5, 2, 3), (4, 5, 6)])
b
# array([[1.5, 2. , 3. ],
#        [4. , 5. , 6. ]])

# specify type of array
c = np.array([[1, 2], [3, 4]], dtype=complex)
c
# array([[1.+0.j, 2.+0.j],
#        [3.+0.j, 4.+0.j]])

# create array with placeholder to minimize the necessity of growing arrays
np.zeros((3, 4))
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])

np.ones((2, 3, 4), dtype=np.int16)
# array([[[1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]],

#        [[1, 1, 1, 1],
#         [1, 1, 1, 1],
#         [1, 1, 1, 1]]], dtype=int16)

np.empty((2, 3))
# array([[1.5, 2. , 3. ],
#        [4. , 5. , 6. ]])

# create sequences of numbers
np.arange(10, 30, 5)  # array([10, 15, 20, 25])
np.arange(0, 2, 0.3)  # array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])

# 9 numbers from 0 to 2
np.linspace(0, 2, 9)  # array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
