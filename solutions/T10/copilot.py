from collections import deque


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = deque()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.cache) == self.capacity:
            oldest = self.queue.popleft()
            del self.cache[oldest]
        self.cache[key] = value
        self.queue.append(key)
