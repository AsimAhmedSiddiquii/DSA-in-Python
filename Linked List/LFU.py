import random


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node(self, node: Node):
        # Add node after Head Node
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_tail(self):
        if self.head.next == self.tail:
            return None
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freqMap = {}
        self.minFreq = 0
        self.hit = 0
        self.miss = 0

    def update(self, node: Node):
        # Get the current frequency of the node
        freq = node.freq
        # Remove the node from the current frequency list
        self.freqMap[freq].remove_node(node)
        # If the frequency list is empty after removing the node,
        # and this frequency was the minimum frequency, update the minimum frequency
        if not self.freqMap[freq].head.next.key and self.minFreq == freq:
            del self.freqMap[freq]  # Delete the empty frequency list from the map
            self.minFreq += 1  # Increment the minimum frequency

        # Increase the node's frequency
        node.freq += 1
        # Get the new frequency of the node
        freq = node.freq
        # If the new frequency does not have a list yet, create one
        if freq not in self.freqMap:
            self.freqMap[freq] = DoublyLinkedList()
        # Add the node to the new frequency list
        self.freqMap[freq].add_node(node)

    def get(self, key: int):
        if key not in self.cache:
            self.miss += 1
            print(f"Cache Miss - {key} #Miss: {self.miss}")
        else:
            node = self.cache[key]
            self.update(node)
            self.hit += 1
            print(f"Cache Hit! {key} : {self.cache[key].value} #Hit: {self.hit}")

    def put(self, key: int, value: int):
        if self.capacity == 0:
            print("Cache Capacity should be greater than 0")
        else:
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self.update(node)
            else:
                if len(self.cache) >= self.capacity:
                    lfu_list = self.freqMap[self.minFreq]
                    lfu_node = lfu_list.pop_tail()
                    del self.cache[lfu_node.key]
                # Create Node
                new_node = Node(key, value)
                # Add Node in Cache
                self.cache[key] = new_node
                # If Freq 1 not in Freq Map
                if 1 not in self.freqMap:
                    # Create Freq Map for 1
                    self.freqMap[1] = DoublyLinkedList()
                # Add the new node to freq map 1
                self.freqMap[1].add_node(new_node)
                # Increase the minimum frequency to 1
                self.minFreq = 1

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print()


cache = LFUCache(10000)
for i in range(100000):
    cache.put(i, i)
    cache.get(random.randint(0, i))
cache.printLL()
