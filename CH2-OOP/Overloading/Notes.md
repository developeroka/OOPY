### Overloading

#### Operator Overloading

More info [here](https://www.w3schools.com/python/python_operators.asp).

1. Author of a class may provide a definition for what happens when an operator is used
2. Uses a specially named method
3. For instance, `a+b` is really `a.__add__(b)`. The latter is called the operator's natural semantic. Thus, we can define a method named `def __add__` and decide what happens when the operator is used. 
4. When a binary operator is applied to two (2) instances of different types like `3 * 'python'`, Python gives deference to the class on the left, checking if `int` class has the `__mul__`, and if it doesn't implement such behavior, it checks the right `str` type via `__rmul__`.


#### Non-Operator Overloading


1. There are specially named methods that impact the behavior of various other functionality to user-defined classes.
2. `str(foo)` is formally a call to the constructor for the `String` class. It calls a special method `foo.__str__()` that should return an appropriate string representation of the class.
3. By Non-Operator it is meant various similar special methods used to determine behavior of objects with the use of `int`, `float` or `bool` based on a parameter from an user define class, i.e. `def __bool__:`. This relates to the notorious an common use of expressions such as `if foo:`, that can be used although `foo` is not *formally* a `Boolean`.

#### Implied methods

There is a general rule and a special.

##### General

If particular method is not implemented ina user defined class, the standard syntax that relies upon that method will raise exception, i.e. `foo + bar` will raise exception if `__add__` OR `__radd__` not defined

##### Special

1. Some operators have default definitions in absence of special methods
2. Some operators whose definition are derived from others, i.e. `__bool__` implies every object other than `None` is evaluated as `True`, in addition to returning `True` for instances of nonzero length only if there is a `__len__` function defined for that class; i.e. `__iter__` returns an iterator of self if the container class hasimplementations for `__len__` AND `__getitem__`; i.e. for classes not having `__eq__` defined, it returns `bool` for expression such as `foo == bar`  evaluating it as `foo is bar` (knowing that an instance is only equivalent to itself and no others)
3. Not everything is automatic, i.e. `__eq__` definition doesn't imply *not equal* `__ne__`; i.e. `__lt__` OR `a < b` **does** imply `__gt__` OR `a > b` **but** providing both *less than* and *equal than* doesn't imply `a <= b` *less than OR equal than*.

### Iterators

1. Supports `__next__` that returns next element of collection or raises `StopIteration` exception to indicate no further elements
2. Generator syntax automatically produces an iterator
3. Automatic iterator implementation for any class that defines both `__len__` AND `__getitem__`

### Dictionaries and `__slots__` Declaration

1. By default, Python represents each namespace with an instance of the built-in dictionary that wraps names in scope to associated objects in a *key*: *value* fashion
2. `__slots__` can be defined to avoid use of the default dictionary by assigning a fixed number of strings to serve as names for instance variables, i.e. `__slots__ = '_customer', '_bank', '_account'`