class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
     
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * self.capacity

    def hash(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        pair = Pair(key, value)
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = pair
                return
            else:
                index = (index + 1)
                index = self.hash(index)
        self.map[index] = pair
        self.size += 1
        if self.size >= self.capacity / 2:
            self.resize()


    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            else:
                index += 1
                index = self.hash(index)
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            else:
                index = (index + 1) % self.capacity
        
        return False

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity  


    def resize(self) -> None:
        newMap = []
        self.capacity = 2 * self.capacity
        for n in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair.key, pair.value)

