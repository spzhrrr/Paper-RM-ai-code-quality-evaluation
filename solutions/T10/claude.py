from collections import OrderedDict


class LRUCache:
    """Least Recently Used (LRU) cache with O(1) average get and put.

    Implemented using OrderedDict, which maintains insertion order and
    supports O(1) move-to-end, enabling efficient LRU tracking without
    a manual doubly-linked list.

    Args:
        capacity: Maximum number of key-value pairs to store.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self._capacity = capacity
        self._cache: OrderedDict = OrderedDict()

    def get(self, key: int) -> int:
        """Return the cached value for key, or -1 if absent.

        Marks the accessed entry as most-recently used.
        Time complexity: O(1) average.
        """
        if key not in self._cache:
            return -1
        self._cache.move_to_end(key)
        return self._cache[key]

    def put(self, key: int, value: int) -> None:
        """Insert or update key with value.

        Evicts the least-recently-used entry if capacity is exceeded.
        Time complexity: O(1) average.
        """
        if key in self._cache:
            self._cache.move_to_end(key)
        else:
            if len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)
        self._cache[key] = value
