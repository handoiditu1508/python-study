# remove item
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)  # [1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)  # [1, 66.25, 1234.5]
del a[:]
print(a)  # []

# delete entire variable
del a
