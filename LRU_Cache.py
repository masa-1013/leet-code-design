class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache.pop(key)
        self.cache[key] = value

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        if len(self.cache) >= self.capacity:
            delete_key = list(self.cache.keys())[0]
            self.cache.pop(delete_key)

        self.cache[key] = value


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
lRUCache.put(4, 4)
print(lRUCache.get(1))
print(lRUCache.get(3))
print(lRUCache.get(4))
