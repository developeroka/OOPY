class Range:
    """
    implement built-in range class
    as an example of iterator
    """
    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        # ‌ calculate the length
        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._stop = stop
