# set is an unordered collection with no duplicate elements
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket)  # {'orange', 'banana', 'pear', 'apple'}
print("orange" in basket)  # True
print("crabgrass" in basket)  # False

# operations
a = set("abracadabra")
b = set("alacazam")
# unique letters in a
print(a)  # {'a', 'r', 'b', 'c', 'd'}
# letters in a but not in b
print(a - b)  # {'r', 'd', 'b'}
# letters in a or b or both
print(a | b)  # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# letters in both a and b
print(a & b)  # {'a', 'c'}
# letters in a or b but not both
print(a ^ b)  # {'r', 'd', 'b', 'm', 'z', 'l'}

# create empty set
empty = set()
print(empty)  # set()

# set comprehensions
a = {x for x in "abracadabra" if x not in "abc"}
print(a)  # {'r', 'd'}
