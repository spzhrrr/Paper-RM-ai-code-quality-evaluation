class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count
