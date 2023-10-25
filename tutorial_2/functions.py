# write Fibonacci series up to n
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


fib(2000)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

print(fib)  # <function fib at 0x00000>
f = fib
f(100)  # 0 1 1 2 3 5 8 13 21 34 55 89

# function without returning value returns None
print(fib(0))  # None


# return Fibonacci series up to n
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fib2(100))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# default arguments
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    pass


ask_ok("Do you really want to quit?")  # giving only the mandatory argument
ask_ok("OK to overwrite the file?", 2)  # giving one of the optional arguments
ask_ok(
    "OK to overwrite the file?", 2, "Come on, only yes or no!"
)  # giving all arguments


# keyword arguments
def parrot(voltage, state="a stiff", action="voom", type="Norwegian Blue"):
    pass


# valid
parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action="VOOOOOM")  # 2 keyword arguments
parrot(action="VOOOOOM", voltage=1000000)  # 2 keyword arguments
parrot("a million", "bereft of life", "jump")  # 3 positional arguments
parrot("a thousand", state="pushing up the daisies")  # 1 positional, 1 keyword

# invalid
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# *name receives a tuple containing the positional arguments beyond the formal parameter list
# **name receives a dictionary containing keyword arguments beyond the formal parameter list
# *name must occur before **name
def cheeseshop(kind, *arguments, **keywords):
    print("kind:", kind)
    for arg in arguments:
        print(arg)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop(
    "Limburger",
    "It's very runny, sir.",
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch",
)
# kind: Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch


# restrict argument type
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only


def standard_arg(arg):
    print(arg)


standard_arg(2)  # valid
standard_arg(arg=2)  # valid


def pos_only_arg(arg, /):
    print(arg)


pos_only_arg(1)  # valid
# pos_only_arg(arg=1)  # invalid


def kwd_only_arg(*, arg):
    print(arg)


kwd_only_arg(arg=3)  # valid
# kwd_only_arg(3)  # invalid


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


combined_example(1, 2, kwd_only=3)  # valid
combined_example(1, standard=2, kwd_only=3)  # valid
# combined_example(1, 2, 3)  # invalid
# combined_example(pos_only=1, standard=2, kwd_only=3)  # invalid


# argument name collision between
# the positional argument name and **kwds which has name as a key
def foo(name, **kwds):
    return "name" in kwds


# foo(1, name=123)  # invalid


# valid name collision
def foo(name, /, **kwds):
    return "name" in kwds


foo(1, name=123)  # valid


# unpacking argument lists
print(list(range(3, 6)))  # [3, 4, 5]
args = [3, 6]
print(list(range(*args)))  # [3, 4, 5]


# unpacking argument dictionary
def parrot(voltage, state="a stiff", action="voom"):
    pass


parrot(voltage="four million", state="bleedin' demised", action="VOOM")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# hover my_function function name to see its documentations
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything."""
    pass


print(my_function.__doc__)


# hover my_function_2 function name to see its annotations
def my_function_2(ham: str, eggs: str = "eggs") -> str:
    return ham + " and " + eggs


print("Annotations:", f.__annotations__)
