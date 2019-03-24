class SequenceIterator:
    """An iterator for any of Python's sequence types"""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence
        self._k = -1
