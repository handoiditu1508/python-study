words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))
# cat 3
# window 6
# defenestrate 12

# iterate over a sequence of numbers
for i in range(5):
    print(i, end=",")
print()
# 0,1,2,3,4,

# iterate over the indices of a sequence
a = ["Mary", "had", "a", "little", "lamb"]
for i in range(len(a)):
    print(i, a[i])
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

# break
for i in range(5):
    if i == 3:
        break
    print(i, end=",")
print()
# 0,1,2,

# In a for loop, the else clause is executed after the loop reaches its final iteration
for i in range(5):
    print(i, end=",")
else:
    print("for else")
# 0,1,2,3,4,for else

# the else clause is not executed if the loop was terminated by a break
for i in range(5):
    if i == 3:
        break
    print(i, end=",")
else:
    print("for else")
print()
# 0,1,2,

# continue
for num in range(2, 10):
    if num % 2 != 0:
        continue
    print(num, end=",")
# 2,4,6,8,
