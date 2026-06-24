class Node:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addLast(self, node):
        temp = self.tail.prev
        temp.next = node
        node.prev= temp
        node.next = self.tail
        self.tail.prev = node

    def removeFirst(self) -> Node:
        temp = self.head.next
        self.remove(temp)
        return temp
    
    def remove(self, node):
        prev = node.prev
        nextval = node.next
        prev.next = nextval
        nextval.prev = prev

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self.remove(node)
        self.addLast(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.addLast(node)
            return

        if len(self.hashmap) >= self.capacity:
            node = self.removeFirst()
            del self.hashmap[node.key]

        node = Node(key, value)
        self.hashmap[key] = node
        self.addLast(node)


        

"""
put
1. get op
fetch from dict the node address
we remove from LL and add it at tail

2. put
if < capacity
    add
else
    remove head at LL
    remove drom dict
    add
add to LL tail

"""