class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""

    # ------------------------------ nested Item class ------------------------------
    class _Item:

        __slots__ = '_value', '_count'                      # streamline memory usage

        def __init__(self, e):

            self._value = e                                 # the user's element
            self._count = 0                                 # access count initially zero
