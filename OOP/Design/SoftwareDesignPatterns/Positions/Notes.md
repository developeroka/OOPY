# The Position Pattern

## Context

To be able to identify a position of an element in a squence without the use of an integer index. 

Examples: 

* a word processor uses the abstraction of a cursor to describe a position within a document without explicit use of an integer index, allowing operations such as: *delete the character at the cursor* or *insert a new character just after the cursor*.
* refering to an ingerent position within a document, such as the beginning of a particular section, without relying on a character index.


## Template

* An independent *position* abstraction to denote the location of an element within a list
* A complete positional list abstract data type (ADT) that can encapsulate a doubly linked list.
* A position acts as a marker or token within a broader positional list.
* A position *p* is unaffected by changes elsewhere in a list, unless it is explicitly deleted.

## Result

### LinkedList example

|Operation|Description
|-|-
`p.element()`|Returns element stored at position `p`.
`L.first()`|Return associated position of first element of L, or `None` if `L` is empty
`L.last()`|Return associated position of last element of `L`, or `None` if `L` is empty
`L.before(p)`|Return position of L immediately before position `p`, or `None` if `p` is the first position.
`L.is_empty()`|Return `True` if list `L` does not contain any elements
`L.add_first(e)`|Insert new element `e` at front of `L`, returning position of new element
`L.add_last(e)`|Insert new element `e` at back of `L`, returning position of new element
`L.add_before(p, e)`|Insert new element `e` just before position `p` in `L`, returning position of new element
`L.add_after(p, e)`|Insert new element `e` just after position `p` with element `e`, returning the element formerly at position `p`
`L.replace(p, e)`|Replace element at position `p` with element `e`, returning element formerly at position `p`
`L.delete(p)`|Remove & return element at position `p` in `L`, invalidating the position

### Tree example

An element is stored at each position, and positions satisfy parent-child relationships that define the tree structure.

|Operation|Description|
|-|-|
|`p.element()`|Return element stored at position `p`
|`T.root()`|Return position of the root of tree `T`, or `None` if `T` is empty
|`T.is_root()`|Return position of the root of tree `T`, or `None` if `T` is empty
|`T.parent(p)`|Return position of parent of position `p`, or `None` if `p` is the root of `T`
|`T.num children(p)`|Return number of children of position `p`


Notes:

* `first()` and `last()` do not return the element
* the first element of a positional list can be determined with `L.first().element()`
* advantage of receiving a position is we can use position to navigate list



### Example Code 

Please refer to [DoublyLinkedList.py]() and [Tree.py]() for an implementation of a `PositionalList` class using a doubly link list wherein each method runs in worst-case O(1).