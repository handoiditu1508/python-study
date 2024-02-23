import fibo

fibo.fib(1000)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
print(fibo.fib2(100))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(fibo.__name__)  # fibo

# assign it to a local name
fib = fibo.fib
fib(500)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# imports names from a module directly
from fibo import fib, fib2

fib(500)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# import all names that a module defines
from fibo import *

fib(500)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# import module as alias
import fibo as fib

fib.fib(500)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from fibo import fib as fibonacci

fibonacci(500)  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

import sys

# built-in function dir() is used to find out which names a module defines
import fibo

dir(fibo)  # ['__name__', 'fib', 'fib2']
dir(sys)
