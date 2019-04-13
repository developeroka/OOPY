# The Composition Pattern

According to a StackOverflow post [here](https://stackoverflow.com/questions/9071067/design-patterns-composite-vs-composition#9071207), the following should be noted: 
* Composition is really a design concept and not really a design pattern
* Should not be confused with the Composite pattern
* Implies **strong ownership** (manages the lifecycle of another object)
* Should not be confused with aggregation (that does not imply ownership).
* Occurs often in Composition over Inheritance discussions

## Context

When a single object is needed to contain other objects, i.e. a priority queue that needs to keep track of an element and its key, even as items are relocated.

## Template

In a priority queue, composition is used to store items internally as *key*, *value* pairs.

## Result

Implementing the composition concept, in a priority queue context, a `PriorityQueueBase` base class is created that includes a nested class `_Item` that is used to store *key*, *value* pairs for all item instances. Please refer to the [examples](https://github.com/developeroka/HiPy/tree/master/OOP/Design/SoftwareDesignPatterns/Structurals/Compositions/examples).