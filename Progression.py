class Progression:

    def __init__(self, start=0):
        """Initialize current to the first value of the progression"""
        self._current = start

    def _advanced(self):
        """update self._current to a new value.

        This should be overridden by a subclass to customize progression.
        """
        self._current += 1

    def __next__(self):

        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advanced()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

