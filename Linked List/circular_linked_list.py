class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            temp = temp.next
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def deleteNode(self):
        curr = self.head
        if self.head == None:
            print("Linked List is Empty!")
        elif curr.next == self.head:
            self.head = None
        else:
            prev = Node()
            while curr.next != self.head:
                prev = curr
                curr = curr.next
            
            prev.next = self.head
    
    def print(self):
        if self.head == None:
            print("Linked List is Empty!")
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
            if temp == self.head:
                break

linkedlist = LinkedList()
linkedlist.insertNode(10)
linkedlist.insertNode(20)
linkedlist.insertNode(30)
linkedlist.deleteNode()
linkedlist.deleteNode()
linkedlist.insertNode(30)
linkedlist.deleteNode()
linkedlist.deleteNode()
linkedlist.print()
