is_hot = True
is_cold = True

print("-" * 10, "if-elif-else", "-" * 10)

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

print("-" * 10, "and-or-not", "-" * 10)

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan (maybe)")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan (not criminal)")

print("-" * 10, "> < ==", "-" * 10)

temperature = 35

if temperature > 30:
    print("It's a hot day")
if temperature < 30:
    print("It's a cold day")
if temperature == 30:
    print("It's a warm day")
