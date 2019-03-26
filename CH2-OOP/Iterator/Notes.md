### Iterators

1. Supports `__next__` that returns next element of collection or raises `StopIteration` exception to indicate no further elements
2. Generator syntax automatically produces an iterator
3. Automatic iterator implementation for any class that defines both `__len__` AND `__getitem__`