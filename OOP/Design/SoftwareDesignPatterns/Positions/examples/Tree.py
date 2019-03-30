class Tree:
    """Abstract base class representing a tree structure."""

    # ------------------------------- nested Position class -------------------------------

    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)            # opposite of eq
