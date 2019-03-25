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

        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._step = step

    def __len__(self):

        return self._length

    def __getitem__(self, item):

        if item < 0:
            item += len(self)

        if not 0 <= item < self._length:
            raise IndexError('index out of range')

        return self._start + item * self._step

    def __str__(self):

        self._list = [self.__getitem__(i) for i in range(0, self._length)]

        return '(' + str(self._list) + ')'


if __name__ == '__main__':
    print(Range(1, 112, 5))
