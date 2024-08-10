import random


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.miss = 0
        self.hit = 0

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node: Node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def moveToTail(self, node: Node):
        self.removeNode(node)
        self.addNode(node)

    def get(self, key: int):
        if key in self.cache:
            node = self.cache[key]
            self.moveToTail(node)
            self.hit += 1
            print(f"Cache Hit! Found {key} : {self.cache[key].value} - {self.hit}")
        else:
            self.miss += 1
            self.put(key, key)
            print(f"Cache Miss - {self.miss}")

    def put(self, key, value):
        if key in self.cache:
            self.moveToTail(self.cache[key])
        else:
            node = Node(key, value)
            self.addNode(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                remove_node = self.head.next
                self.removeNode(remove_node)
                del self.cache[remove_node.key]
        # self.printLL()

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print()


cache = LRUCache(10000)
for i in range(100000):
    cache.put(i, i)
    cache.get(random.randint(0, i))
cache.printLL()
