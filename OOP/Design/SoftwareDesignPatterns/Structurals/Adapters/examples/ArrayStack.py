class ArrayStack:

    def __init__(self):

        self._data = []

    def __len__(self):

        return len(self._data)

    def is_empty(self):

        return len(self._data) == 0

    def push(self, e):

        self._data.append(e)

    def top(self):

        if len(self._data) == 0:
            raise Empty('Stack is empty')
        else:
            return self._data[-1]

    def pop(self):

        if len(self._data) == 0:
            raise Empty('Stack is empty')
        else:
            return self._data.pop()

    def __str__(self):

        return str(self._data[0:len(self._data) + 1])


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


if __name__ == '__main__':

    stack = ArrayStack()
    stack.push(5)
    print(stack)
    stack.push(3)
    stack.push(4)
    stack.pop()
    print(stack.top())
    stack.pop()
    print(stack.is_empty())
