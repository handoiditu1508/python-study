numbers = (1, 2, 3, 4)

# numbers[0] = 10 # will show error, tuple object is immutable
print(numbers[0])

# declare tuple without parentheses
numbers2 = 1, 2, 3, 4

print(numbers == numbers2)  # True

# spread operator like javascript
[a, b, *rest] = numbers2
print(rest)  # [3, 4]

# check tuple contains value
print(3 in numbers)  # True
