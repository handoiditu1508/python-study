numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(1)
print(numbers)

numbers.pop()
print(numbers)

# print(numbers.index(50)) # will show error since 50 is not in numbers
print(50 in numbers)

numbers.append(3)
numbers.append(3)
print(numbers.count(3))

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

cloned_numbers = numbers.copy()
cloned_numbers.append(6)
print(numbers, cloned_numbers)

numbers.clear()
print(numbers)
