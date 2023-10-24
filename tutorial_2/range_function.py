# range() return an iterable that act like a list
# but it doesn’t really make the list, thus saving space
print(list(range(5)))  # [0, 1, 2, 3, 4]
print(list(range(5, 10)))  # [5, 6, 7, 8, 9]
print(list(range(0, 10, 3)))  # [0, 3, 6, 9]
print(list(range(-10, -100, -30)))  # [-10, -40, -70]
