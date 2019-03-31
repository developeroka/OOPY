class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'       # streamline memory

        def __init__(self, element, prev, next):        # initialize node’s fields
            self._element = element                     # user’s element
            self._prev = prev                           # previous node reference
            self._next = next                           # next node reference

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer              # trailer is after header
        self._trailer._prev = self._header              # header is before trailer
        self._size = 0                                  # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)  # linked to neighbors
        predecessor. next = newest
        successor. prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete non sentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                         # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element                                  # return deleted element


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # -------------------------- nested Position class --------------------------

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)                       # opposite of eq

