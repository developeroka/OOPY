# The Template Method Pattern



## Context

The template pattern is used to provide a framework for the reuse and adaptation of generic behavior that can be *specialized* for a particular implementation by defining or redefining (overriding) some of its methods.

## Template (how)

By using [Abstract Base Classes](https://docs.python.org/3/glossary.html#term-abstract-base-class),  we declare`ABCMeta` of the `abc` [module](https://docs.python.org/3/library/abc.html#module-abc) as a metaclass on our class to assure that the constructor of the subclass raises an error if it does not provide a concrete implementation of all desired core behaviors labeled with the @abstractmethod decorator. This enforces the notion or idea of a *template* to be followed by any class that inherits from it:

```python
from abc import ABCMeta

class MyTemplate(metaclass=ABCMeta):
    @abstractmethod
    def my_core_behavior_to_be_implemented(self):
        raise NotImplemented
```

## Result (output)

An example of this pattern can be found in Python's `collections.abc` module ([docs here](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes), [source code here](https://github.com/python/cpython/blob/3.7/Lib/_collections_abc.py)), that assist in the creation of user-defined classes:

1. [`collections.abc.Sequence`](https://github.com/python/cpython/blob/be63df287a4a12ad86b4a2aec4358a1309f0488b/Lib/_collections_abc.py#L865), a class that provides concrete implementations of behaviors common to `list`, `str`, and `tuple` classes like iteration via `__iter__`, membership test via [`__contains__`](https://docs.python.org/3/reference/datamodel.html#object.__contains__), reverse iteration via [`__reversed__`](https://docs.python.org/3/reference/datamodel.html#object.__reversed__), index lookup via `index`, and number of occurrence of a value via `count`; all of which could be inherited by any class that provide concrete implementations of both `__len__` and `__getitem__`. 
2. [`collections.abc.Mapping`](https://github.com/python/cpython/blob/7723d0545c3369e1b2601b207c250c70ce90b75e/Lib/_collections_abc.py#L641), a class for a generic container for associating key/value pairs that provide concrete implementations of all mapping methods: `get()`,`__contains__`, `keys()`, `items()`, `values()`, and `__eq__`; all of which could be inherited by any class that provide concrete implementations of `__getitem__`, `__iter__`, and `__len__`.
3. [`collections.abc.MutableMapping`](https://github.com/python/cpython/blob/7723d0545c3369e1b2601b207c250c70ce90b75e/Lib/_collections_abc.py#L767), a class for a generic container for associating key_value pairs that inherits from `collections.abc.Mapping` and provides concrete generic implementations for removing a specified key and returning its value via `pop()`, removing and returning some key, value pair as a 2-tuple via `popitem()`, removing all items from a mapping via `clear()`,  updating from mapping or iterable via `update()`, and getting a value from a key and updating its value if its not found via`setdefault()`; all of which could be inherited by any class that provide concrete implementations of `__getitem__`, `__setitem__`, `__delitem__`, `__iter__` and `__len__`.
4. [`collections.abc.MutableSet`](https://github.com/python/cpython/blob/7723d0545c3369e1b2601b207c250c70ce90b75e/Lib/_collections_abc.py#L556), which inherits from `collections.abc.Set`, a finite, iterable container, that provides concrete generic implementations for `remove()`, `pop()`, `clear()`, `__ior__`, `__iand__`, `__ixor__` and `__isub__`; all of which could be inherited by any class that provide concrete implementations of `add()`, `discard()`, `__contains__`, `__iter__`, and `__len__`.

### Example Code

For additional code samples, please see [here](https://github.com/developeroka/HiPy/tree/master/OOP/Design/SoftwareDesignPatterns/Behaviorals/TemplateMethods/examples).