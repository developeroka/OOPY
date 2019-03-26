# OOP

## Goals, Principles and Patterns

### OOP Design Goals

#### Robustness

* Having the right output for anticipated inputs.
* Able to handle unexpected inputs not explicitly defined for its application.

#### Adaptability

* Able to evolve over time in response to changing conditions in its environment.
* Ability of software to run with minimal change on different hardware and OS platform.

#### Reusability

* Same code should be usable as a component of different systems in various applications

### OOP Design Goals Facilitators

#### Modularity

1. Different components must interact correctly
2. Different components must be well organized
3. Different components are divided into separate functional units
4. Collection of closely related functions and classed defined together in a single file
5. Support Robustness; it's easier to test & debug separate components before integration
6. Structure imposed by modularity helps enable software reusability

#### Abstraction

1. Distill to fundamental parts
2. Involves naming and explaining functionality
3. Abstract Data Types (ADT) is a mathematical model of a Data Structure that specifies the data stores, the operations supported and types of parameters of operations; **specifies what** each operation does **but not how**.

#### Encapsulation

1. Components shouldn't reveal internal details of implementation
2. Freedom to implement details of components without concern that other programmer will write code that depends on those details
3. Yields robustness and adaptability because it allows implementation details of parts of the program to change without affecting other parts, thus making it easier to fix bugs or add new functionality with local changes to a component.
4. Python provides loose support for encapsulation (`_var` is assumed non-public)

### Design Patterns

1. Solution to typical software design problems
2. Tamplate to be applied in many different situations
3. Consists of a **name**, **context** or *scenarios* to be applied, **template** or *how* the pattern is applied, and **result** or *analysis of output* produced.
4. Its divided into two groups: algorithm deign problems and software engineering problems.

### Software Development

It consists of three (3) major steps:

1. Design
2. Implementation
3. Testing and Debugging

#### Design

1. Decide workings of program into classes
2. How classes will interact
3. What data each class will store
4. What actions each class will perform

##### Rules of Thumb:

1. Responsibilities
2. Independence
3. Behaviors

###### Responsibilities

1. Different actors (division of labor)
2. Describe responsibilities using action verbs
3. Actors will be classes for the program

###### Independence

1. Work for each class to be independent from others
2. Subdivide responsibilities between classes so that each class has autonomy over some aspect of the program
3. Give data to class with jurisdiction over actions that require access to this data

###### Behaviors

1. Define behaviors of each class *carefully* and *precisely* so consequences of each action performed is well understood by other classes that interact with it
2. Behaviors will define methods that htis class performs
3. Set of behaviors for a class are the interface to the class, as they form the means for other pieces of code to interact with object from the class.

#### Design Process

1. Iterates trough a action/actor cycle
2. Identify action (responsibility), then identify actor (component) to peform action
3. Design is complete when we have assigned all actions to actors
4. Using index cards guarantees small set of responsibilities (rember CRC's)

##### UML Class Diagram

1. Consists of three portions: name, recommended instance variables, recommended methods of the class

#### Testing and Debugging

1. Testing is to check correctneess of a program
2. Debugging is tracking execution of a program and discover errors in it

##### Main strategies for testing

1. Top-down goes from the top to the bottom of the program hierarchy
2. Bottom-up goes from low level components to higher level

### Class Definitions

1. Clas is primary means of abstraction in  OOP
2. Every piece of data is represented as an instance of some class
3. Class provides set of behaviors in form of member functions or methods
4. Class serves as a blueprint for its instances, determining the way that state information for each instance is represented in the form of attributes.

### Encapsulation

1. Non-public data members allows for batter enforcement of consistent state for all instances
2. Get and Setters for non-public variables
3. Allows for greater flexibility to redesign the way a class works, perhaps to improve the efficiency of the structure

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

### Inheritance

1. From general to specific
2. The correspondence is in regards to a **"is a" relationship**, as in **A Cat *is an* Animal**
3. Common functionality can be grouped at the most general level
4. Modular and hierarchical organization is called inheritance
5. A subclass may: (a) **specialize** and existing behavior in a new implementation OR (b) **extend** by providing a new method

### Protected Members
In Python, there are `_protected` and `__private` member methods:
1. `_protected` accessible to subclasses
2. `__private` accesible to neither

### Abstract Base Classes (ABC)

1. If its only puprpose is to serve as a base class
2. Can't be directly instantiates
3. Guarantees one or more abstract methods
4. A so called template method pattern provides: concrete behaviors that rely upon calls to other abstract behaviors; as soon as subclass implements these behaviors, the inherited behaviors are concretely defined; i.e. the `collections.Sequence` class provides concrete implementations of methods `count`, `index` and `contains` that can be inherited by any class that provides concrete implementations of both `__len__` and `__getitem`.

### Namespaces

1. Manages all function identifiers in a particular scope
2. Maps each name to its associated value

### Class Data Members

1. Used when there is some value, such as a constant; and
2. Is shared by all instances of a class
3. By concention this class variable is defined in all caps, i.e. `PI = 3.14159 `

### Nested Classes

1. Unrelated to inheritance
2. Nested classes exist to support outer class

### Dictionaries and `__slots__` Declaration

1. By default, Python represents each namespace with an instance of the built-in dictionary that wraps names in scope to associated objects in a *key*: *value* fashion
2. `__slots__` can be defined to avoid use of the default dictionary by assigning a fixed number of strings to serve as names for instance variables, i.e. `__slots__ = '_customer', '_bank', '_account'`

### Name Resolution and Dynamic Dispatch

Pythons lookup goes like this:

1. Instance Namespace
2. Class Namespace
3. Upward search through inheritance hierarchy
4. Check class namespace for each ancestor
5. Not found raises `AttributeError` 