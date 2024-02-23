t = 12345, 54321, "hello!"
print(t[0])  # 12345
print(t)  # (12345, 54321, 'hello!')

# unpacking
x, y, z = t

# Tuples may be nested
u = t, (1, 2, 3, 4, 5)
print(u)  # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
# t[0] = 88888
# TypeError: 'tuple' object does not support item assignment
# but they can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])

# empty tuple
empty = ()
print(len(empty))  # 0

# single tuple
singleton = ("hello",)
print(len(singleton))  # 1
