from OOP.Design.SoftwareDesignPatterns.Structurals.Compositions.examples import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []
