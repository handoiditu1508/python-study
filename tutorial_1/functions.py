def greet_user():
    print("Hi there!")
    print("Welcome aboard")


print("Start")
greet_user()
print("Finish")

print("-" * 10, "parameters", "-" * 10)


def great_user_2(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


great_user_2("John", "Doe")
great_user_2("John", last_name="Smith")


print("-" * 10, "return statement", "-" * 10)


def square(number):
    return number * number


print(square(3))
