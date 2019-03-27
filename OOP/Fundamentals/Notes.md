# Fundamentals

## Class Definitions

1. Class is primary means of abstraction in  OOP
2. Every piece of data is represented as an instance of some class
3. Class provides set of behaviors in form of member functions or methods
4. Class serves as a blueprint for its instances, determining the way that state information for each instance is represented in the form of attributes.

## Encapsulation

1. Non-public data members allows for batter enforcement of consistent state for all instances
2. Get and Setters for non-public variables
3. Allows for greater flexibility to redesign the way a class works, perhaps to improve the efficiency of the structure

## Inheritance

1. From general to specific
2. The correspondence is in regards to a **"is a" relationship**, as in **A Cat *is an* Animal**
3. Common functionality can be grouped at the most general level
4. Modular and hierarchical organization is called inheritance
5. A subclass may: (a) **specialize** and existing behavior in a new implementation OR (b) **extend** by providing a new method

### Abstract Base Classes (ABC)

1. If its only puprpose is to serve as a base class
2. Can't be directly instantiates
3. Guarantees one or more abstract methods
4. A so called template method pattern provides: concrete behaviors that rely upon calls to other abstract behaviors; as soon as subclass implements these behaviors, the inherited behaviors are concretely defined; i.e. the `collections.Sequence` class provides concrete implementations of methods `count`, `index` and `contains` that can be inherited by any class that provides concrete implementations of both `__len__` and `__getitem`.

## Namespaces

1. Manages all function identifiers in a particular scope
2. Maps each name to its associated value

### Protected Members
In Python, there are `_protected` and `__private` member methods:
1. `_protected` accessible to subclasses
2. `__private` accessible to neither

### Class Data Members

1. Used when there is some value, such as a constant; and
2. Is shared by all instances of a class
3. By concention this class variable is defined in all caps, i.e. `PI = 3.14159 `

## Nested Classes

1. Unrelated to inheritance
2. Nested classes exist to support outer class

## Name Resolution and Dynamic Dispatch

Pythons lookup goes like this:

1. Instance Namespace
2. Class Namespace
3. Upward search through inheritance hierarchy
4. Check class namespace for each ancestor
5. Not found raises `AttributeError` 