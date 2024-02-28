# handling exceptions
try:
    raise Exception
except:
    print("Error")

# handling ValueError exceptions
try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oops!  That was no valid number.  Try again...")

# handling multiple exception types
try:
    raise Exception
except (RuntimeError, TypeError, NameError):
    print("Error")


# exception inheritance
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# B
# C
# D

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")
# B
# B
# B

# exception with arguments
try:
    raise Exception("spam", "eggs")
except Exception as inst:
    print(type(inst))  # the exception type
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # unpack args
    print("x =", x)
    print("y =", y)
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs

# re-raise exception
try:
    raise Exception
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

# else clause executes if try clause not raise an exception
try:
    pass
except:
    print("Error")
else:
    print("No error")

# exception chaining
try:
    raise Exception
except Exception as err:
    raise NameError("Hello Error") from err

# finally clause is used for cleaning up
try:
    raise KeyboardInterrupt
finally:
    print("Goodbye, world!")


# raise multiple exceptions together
def f():
    excs = [OSError("error 1"), SystemError("error 2")]
    raise ExceptionGroup("there were problems", excs)


f()
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 1, in <module>
#   |   File "<stdin>", line 3, in f
#   | ExceptionGroup: there were problems (2 sub-exceptions)
#   +-+---------------- 1 ----------------
#     | OSError: error 1
#     +---------------- 2 ----------------
#     | SystemError: error 2
#     +------------------------------------

try:
    f()
except Exception as e:
    print(type(e))  # <class 'ExceptionGroup'>


# using except* to selectively handle exception in group
def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup("group2", [OSError(3), RecursionError(4)]),
        ],
    )


try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
# There were OSErrors
# There were SystemErrors
#   + Exception Group Traceback (most recent call last):
#   |   File "<stdin>", line 2, in <module>
#   |   File "<stdin>", line 2, in f
#   | ExceptionGroup: group1 (1 sub-exception)
#   +-+---------------- 1 ----------------
#     | ExceptionGroup: group2 (1 sub-exception)
#     +-+---------------- 1 ----------------
#       | RecursionError: 4
#       +------------------------------------

# exception notes
try:
    raise Exception
except Exception as err:
    err.add_note("Add some information")
    err.add_note("Add some more information")
    raise
