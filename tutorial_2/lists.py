squares = [1, 4, 9, 16, 25]
print(squares)  # [1, 4, 9, 16, 25]

# indexing returns the item
print(squares[0])  # 1
print(squares[-1])  # 25
# slicing returns a new list
print(squares[-3:])  # [9, 16, 25]

# shallow copy
print(squares[:])  # [1, 4, 9, 16, 25]

# concatenate
print(squares + [36, 49, 64, 81, 100])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# mutate list
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)  # [1, 8, 27, 64, 125]

# add new items at the end of the list
cubes.append(216)
print(cubes)  # [1, 8, 27, 64, 125, 216]

letters = ["a", "b", "c", "d", "e", "f", "g"]
# replace some values
letters[2:5] = ["C", "D", "E"]
print(letters)  # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
print(letters)  # ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)  # []

# length
letters = ["a", "b", "c", "d"]
print(len(letters))  # 4

# spread operator like javascript
[a, b, *rest] = letters
print(rest)  # ['c', 'd']

# lists containing other lists
a = ["a", "b", "c"]
n = [1, 2, 3]
x = [a, n]
print(x)  # [['a', 'b', 'c'], [1, 2, 3]]
print(x[0])  # ['a', 'b', 'c']
print(x[0][1])  # b

# check list contains value
print("a" in letters)  # True
