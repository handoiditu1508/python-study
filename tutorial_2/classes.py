# creating class
class MyClass:
    """A simple example class"""

    i = 12345

    def f(self):
        return "hello world"


MyClass.i  # 12345
MyClass.f  # <function MyClass.f at 0x000001A7101FF100>
MyClass.__doc__  #'A simple example class'

# class instantiation
x = MyClass()
x.i  # 12345
x.f()  # 'hello world'
MyClass.f(x)  # 'hello world'


# class with constructor
class MyClass2:
    def __init__(self) -> None:
        self.data = []


x = MyClass2()
x.data  # []
# MyClass.data # AttributeError: type object 'MyClass' has no attribute 'data'


# constructor with arguments
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
x.r, x.i  # (3.0, -4.5)


# data attributes
class MyClass3:
    pass


x = MyClass3()
x.counter = 16
x.counter  # 16
del x.counter


# class and instance Variables
class Dog:
    kind = "canine"  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


d = Dog("Fido")
e = Dog("Buddy")
d.kind  # 'canine'
e.kind  # 'canine'
d.name  # 'Fido'
e.name  # 'Buddy'
# if class and instance variable have the same name
# attribute lookup prioritizes the instance variable
d.kind = "k9"
Dog.kind = "kx9"
d.kind  # 'k9'
e.kind  # 'kx9'


# Function defined outside the class
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return "hello world"

    h = g


# method may call other methods
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


# Private Variables
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
