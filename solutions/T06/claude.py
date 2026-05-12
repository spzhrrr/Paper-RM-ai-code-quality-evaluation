class _Node:
    """Internal singly-linked-list node."""

    __slots__ = ('value', 'next')

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """LIFO stack backed by a singly linked list.

    All operations run in O(1) time and O(n) space where n is the
    number of elements currently stored.
    """

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, value) -> None:
        """Push value onto the top of the stack."""
        node = _Node(value)
        node.next = self._top
        self._top = node
        self._size += 1

    def pop(self):
        """Remove and return the top element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self._top is None:
            raise IndexError('pop from empty stack')
        value = self._top.value
        self._top = self._top.next
        self._size -= 1
        return value

    def peek(self):
        """Return the top element without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if self._top is None:
            raise IndexError('peek from empty stack')
        return self._top.value

    def is_empty(self) -> bool:
        """Return True if the stack contains no elements."""
        return self._top is None

    def size(self) -> int:
        """Return the number of elements in the stack."""
        return self._size
