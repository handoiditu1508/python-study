a = 0
while a < 10:
    print(a, end=",")
    a += 1
print()
# 0,1,2,3,4,5,6,7,8,9,

# In a while loop, it’s executed after the loop’s condition becomes false
a = 0
while a < 10:
    print(a, end=",")
    a += 1
else:
    print("for else")
# 0,1,2,3,4,5,6,7,8,9,for else

# the else clause is not executed if the loop was terminated by a break
a = 0
while a < 10:
    if a == 3:
        break
    print(a, end=",")
    a += 1
else:
    print("for else")
print()
# 0,1,2,
