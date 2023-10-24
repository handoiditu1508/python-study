# single quotes
print("spam eggs")
# double quotes
print("Paris rabbit got your back :)! Yay!")
# digits and numerals enclosed in quotes are also strings
print("1975")

# use \' to escape the single quote
print("hello 'hello1' \"hello2\"")  # hello 'hello1' "hello2"

# note the r before the quote, r stands for raw
print(r"C:\some\name")  # C:\some\name

# string literals
print(
    """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
)
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
#

# strings can be concatenated (glued together) with the + operator, and repeated with *
print(3 * "un" + "ium")  # unununium

# 2 or more string literals next to each other are automatically concatenated
print("Py" "thon")  # Python
print(
    "Put several strings within parentheses asd asd asd asd asd asd asd asd "
    "to have them joined together."
)  # Put several strings within parentheses asd asd asd asd asd asd asd asd to have them joined together.

# strings can be indexed
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
word = "Python"
print(word[0])  # p
print(word[5])  # n
# last character
print(word[-1])  # n
# second-last character
print(word[-2])  # o
print(word[-6])  # p

# characters from position 0 (included) to 2 (excluded)
print(word[0:2])  # Py
# characters from position 2 (included) to 5 (excluded)
print(word[2:5])  # tho
print(word[:2])  # Py
print(word[2:])  # thon
# out of range slice
print(word[4:42])  # on
print(word[42:])  # ""

# replace
print("J" + word[1:])  # Jython
print(word[:2] + "py")  # Pypy

# length
print(len("supercalifragilisticexpialidocious"))  # 34
