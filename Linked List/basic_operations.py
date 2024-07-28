class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def deleteNode(self):
        if self.head == None:
            print("No Node to delete!")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def deleteVal(self, val):
        temp = self.head
        if self.head == None:
            print("No Node to delete!")
        elif temp.val == val:
            self.head = temp.next
        else:
            prev = Node()
            while temp:
                if temp.val == val:
                    prev.next = temp.next
                prev = temp
                temp = temp.next

    def max(self):
        maxVal = 0
        temp = self.head
        while temp:
            maxVal = max(maxVal, temp.val)
            temp = temp.next
        print(maxVal)

    def min(self):
        temp = self.head
        minVal = temp.val
        while temp:
            minVal = min(minVal, temp.val)
            temp = temp.next
        print(minVal)

    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

linkedlist = LinkedList()
linkedlist.insertNode(10)
linkedlist.insertNode(20)
linkedlist.insertNode(40)
linkedlist.insertNode(30)
linkedlist.insertNode(60)
linkedlist.deleteVal(60)
linkedlist.print()