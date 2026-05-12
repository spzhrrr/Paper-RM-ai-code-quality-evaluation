class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.head.value

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size
