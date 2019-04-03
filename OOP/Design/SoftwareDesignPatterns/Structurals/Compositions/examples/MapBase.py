from collections import MutableMapping


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic Item class"""

    # ------------------------------- nested Item class -------------------------------
    class _Item:
        """”Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
