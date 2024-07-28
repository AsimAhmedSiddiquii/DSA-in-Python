class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.map = {}  # For O(1) removal and searching
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertNode(self, node: Node):  # O(1)
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
        self.map[node.key] = node
        self.printLL()

    def searchNode(self, key: int):  # O(1)
        if key in self.map:
            print(f"Found {key} : {self.map[key].value}")
        else:
            print("Search: Key not Found")

    def removeNode(self, key: int):  # O(1)
        if key in self.map:
            node = self.map[key]
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.printLL()
        else:
            print("Removal: Key not Found")

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print()

    def reverse(self):
        temp = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            self.head = temp
            temp = temp.prev
        self.printLL()


linkedlist = DoublyLinkedList()
linkedlist.insertNode(Node(20, 20))
linkedlist.insertNode(Node(30, 30))
linkedlist.insertNode(Node(40, 40))
linkedlist.removeNode(30)
linkedlist.searchNode(20)
linkedlist.reverse()
