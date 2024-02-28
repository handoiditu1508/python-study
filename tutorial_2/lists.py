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
cubes.append(216)  # equivalent to `cubes[len(cubes):] = [216]`
print(cubes)  # [1, 8, 27, 64, 125, 216]

letters = ["a", "b", "c", "d", "e", "f", "g"]
# replace some values
letters[2:5] = ["C", "D", "E"]
print(letters)  # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
print(letters)  # ['a', 'b', 'f', 'g']
# extend the list by appending all the items from the iterable
letters[len(letters) :] = ["i", "j"]  # equivalent to `letters.extend(["i", "j"])`
print(letters)  # ['a', 'b', 'f', 'g', 'i', 'j']
# Insert an item at a given position
letters.insert(2, "c")
print(letters)  # ['a', 'b', 'c', 'f', 'g', 'i', 'j']
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

# using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)  # [3, 4, 5, 6, 7]
print(stack.pop())  # 7
print(stack)  # [3, 4, 5, 6]
print(stack.pop())  # 6
print(stack.pop())  # 5
print(stack)  # [3, 4]

# using Lists as Queues
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)  # deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
print(queue.popleft())  # Eric
print(queue.popleft())  # John
print(queue)  # deque(['Michael', 'Terry', 'Graham'])

# list comprehensions provide a concise way to create lists
# x still exists after loop completes
squares = []
for x in range(10):
    squares.append(x**2)
print(x)  # 9
# more concise way
squares = list(map(lambda x: x**2, range(10)))
# or using list comprehension
squares = [x**2 for x in range(10)]

# list comprehensions example
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# equivalent to
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# with else statement
combs = [(x, y) if x != y else (0, 0) for x in [1, 2, 3] for y in [3, 1, 4]]
print(combs)  # [(1, 3), (0, 0), (1, 4), (2, 3), (2, 1), (2, 4), (0, 0), (3, 1), (3, 4)]
# equivalent to
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
        else:
            combs.append((0, 0))
print(combs)  # [(1, 3), (0, 0), (1, 4), (2, 3), (2, 1), (2, 4), (0, 0), (3, 1), (3, 4)]

# nested list comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(
    [[row[i] for row in matrix] for i in range(4)]
)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# equivalent to
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# equivalent to
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# equivalent to this built-in function
print(list(zip(*matrix)))  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# looping with index value
for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe

# loop over two or more sequences at the same time
questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print("What is your {0}?  It is {1}.".format(q, a))
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

# loop over a sequence in reverse
for i in reversed(range(1, 10, 2)):
    print(i)
# 9
# 7
# 5
# 3
# 1

# loop over a sequence in sorted order
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for i in sorted(basket):
    print(i)
# apple
# apple
# banana
# orange
# orange
# pear

# comparing sequences and other types
print((1, 2, 3) < (1, 2, 4))  # True
print([1, 2, 3] < [1, 2, 4])  # True
print("ABC" < "C" < "Pascal" < "Python")  # True
print((1, 2, 3, 4) < (1, 2, 4))  # True
print((1, 2) < (1, 2, -1))  # True
print((1, 2, 3) == (1.0, 2.0, 3.0))  # True
print((1, 2, ("aa", "ab")) < (1, 2, ("abc", "a"), 4))  # True
