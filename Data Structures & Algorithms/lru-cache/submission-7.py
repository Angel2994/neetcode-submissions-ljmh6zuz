class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.right = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0, 0)
        self.left.right, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.right
            self.remove(lru)
            del self.cache[lru.key]

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.right = nxt.prev = node
        node.prev, node.right = prev, nxt

    def remove(self, node):
        prev, nxt = node.prev, node.right
        prev.right, nxt.prev = nxt, prev

