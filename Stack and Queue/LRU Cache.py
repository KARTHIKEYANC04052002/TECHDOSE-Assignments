class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.storage = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.storage.remove(key)
            self.storage.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.storage.remove(key)
            self.storage.append(key)
            self.cache[key] = value
        else:
            if len(self.storage) < self.capacity:
                self.storage.append(key)
                self.cache[key] = value
            else:
                del self.cache[self.storage[0]]
                self.storage.pop(0)
                self.cache[key] = value
                self.storage.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)