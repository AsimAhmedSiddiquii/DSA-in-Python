class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
    
class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
            newNode = Node(data)
            newNode.next = self.top
            self.top = newNode
            print(data, 'pushed to Stack!')
            self.display()

    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            popNode = self.top
            self.top = self.top.next
            print(popNode.data, 'popped from Stack!')
            self.display()
        
    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            current = self.top
            while current:
                print(current.data, end=' -> ')
                current = current.next
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.pop()
stack.push(30)