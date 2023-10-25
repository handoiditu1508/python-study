def increase_normal(x):
    return x + 10


# x => x + 10
increase = lambda x: x + 10
print(increase(5))  # 15

# (a, b) => a + b
plus = lambda a, b: a + b

# lambda as argument
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
