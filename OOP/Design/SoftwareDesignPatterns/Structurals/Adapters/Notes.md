# Adapter Pattern

## Context

Used to modify an existing class so that its methods match those of a related, but different class or interface.

## Template

One way to do it:

1. Define a new class containing an instance of the existing class as a hidden field 
2. Implement each method of the new class usng methods of the hidden instance variable

## Result

A new class that parforms some of the same functions as an existing class, but repackaged in a more convenient way.

For example:

|Stack Method|Realization with Python `list`|
|-|-|
S.push(e)|L.append(e)
S.pop()|L.pop()
S.top()|L.[-1]
S.is_empty()|len(L) == 0
len(S)|len(L)

### Example Code

Please refer to [ArrayStack.py](https://github.com/developeroka/mypy/blob/development/OOP/Design/SoftwareDesignPatterns/Structurals/Adapters/examples/ArrayStack.py) for further information.