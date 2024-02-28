tel = {"jack": 4098, "sape": 4139}
tel["guido"] = 4127
print(tel)  # {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel["jack"])  # 4098
print(tel.get("jone", "not found"))  # not found

# delete
del tel["sape"]
tel["irv"] = 4127
print(tel)  # {'jack': 4098, 'guido': 4127, 'irv': 4127}

# list of keys
print(list(tel))  # ['jack', 'guido', 'irv']

# sorted list of keys
print(sorted(tel))  # ['guido', 'irv', 'jack']

# check dictionary has key
print("guido" in tel)  # True
print("jack" not in tel)  # False

# builds dictionaries directly from sequences of key-value pairs
print(
    dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])
)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}

# dict comprehensions
print({x: x**2 for x in (2, 4, 6)})  # {2: 4, 4: 16, 6: 36}

# keys are simple strings
print(
    dict(sape=4139, guido=4127, jack=4098)
)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}

# looping with key value
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave
