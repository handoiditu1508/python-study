import numpy as np

# compute all the a+b*c for all the triplets taken from each of the vectors a, b and c
a = np.array([2, 3, 4, 5])
b = np.array([8, 5, 4])
c = np.array([5, 4, 6, 8, 3])
ax, bx, cx = np.ix_(a, b, c)

ax
# array([[[2]],

#        [[3]],

#        [[4]],

#        [[5]]])

bx
# array([[[8],
#         [5],
#         [4]]])

cx
# array([[[5, 4, 6, 8, 3]]])

ax.shape, bx.shape, cx.shape  # ((4, 1, 1), (1, 3, 1), (1, 1, 5))

result = ax + bx * cx
result
# array([[[42, 34, 50, 66, 26],
#         [27, 22, 32, 42, 17],
#         [22, 18, 26, 34, 14]],

#        [[43, 35, 51, 67, 27],
#         [28, 23, 33, 43, 18],
#         [23, 19, 27, 35, 15]],

#        [[44, 36, 52, 68, 28],
#         [29, 24, 34, 44, 19],
#         [24, 20, 28, 36, 16]],

#        [[45, 37, 53, 69, 29],
#         [30, 25, 35, 45, 20],
#         [25, 21, 29, 37, 17]]])

result[3, 2, 4]  # 17
a[3] + b[2] * c[4]  # 17


# You could also implement the reduce as follows:
def ufunc_reduce(ufct, *vectors):
    vs = np.ix_(*vectors)
    r = ufct.identity  # 0
    for v in vs:
        r = ufct(r, v)
    return r


ufunc_reduce(np.add, a, b, c)
# array([[[15, 14, 16, 18, 13],
#         [12, 11, 13, 15, 10],
#         [11, 10, 12, 14,  9]],

#        [[16, 15, 17, 19, 14],
#         [13, 12, 14, 16, 11],
#         [12, 11, 13, 15, 10]],

#        [[17, 16, 18, 20, 15],
#         [14, 13, 15, 17, 12],
#         [13, 12, 14, 16, 11]],

#        [[18, 17, 19, 21, 16],
#         [15, 14, 16, 18, 13],
#         [14, 13, 15, 17, 12]]])
