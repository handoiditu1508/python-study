print("-" * 10)
print("while loop")
print("-" * 10)

index = 1
while index <= 5:
    if index == 4:
        break
    print(index)
    index += 1
else:  # else on while loop run when loop finished without break
    print("loop finished without break")
print("Done")

print("-" * 10)
print("for loop")
print("-" * 10)

for item in "Python":
    print(item, end=" ")
print()

for item in ["John", "Doe", "Max"]:
    print(item, end=" ")
print()

for item in range(10):
    print(item, end=" ")
print()

for item in range(5, 10):
    print(item, end=" ")
print()

for item in range(5, 10, 2):
    print(item, end=" ")
print()
