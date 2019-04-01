class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""

    # ------------------------------ nested Item class ------------------------------
    class _Item:

        __slots__ = '_value', '_count'                      # streamline memory usage

        def __init__(self, e):

            self._value = e                                 # the user's element
            self._count = 0                                 # access count initially zero

    # ------------------------------- nonpublic utilities -------------------------------
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():                                   # consider moving...
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:                 # must shift forward
                while(walk != self._data.first() and
                      cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delte(p))      # delete/reinsert
