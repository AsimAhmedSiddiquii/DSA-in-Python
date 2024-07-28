class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.front = self.rear = -1

    def enqueue(self, val):
        if (self.rear+1) % self.size == self.front:
            print("Queue is Full")
        elif self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.arr[self.front] = val
        else:
            self.rear = (self.rear + 1) % self.size
            self.arr[self.rear] = val

    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Empty!")
        elif self.front == self.rear:
            self.arr[self.front] = None
            self.front = self.rear = -1
        else:
            self.arr[self.front] = None
            self.front = (self.front + 1) % self.size

    def print(self):
        if self.front == -1:
            print("Queue is Empty!")
        elif self.rear >= self.front:
            for i in range(self.rear+1):
                print(self.arr[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.arr[i], end=" ")
            for j in range(0, self.rear+1):
                print(self.arr[j], end=" ")

queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.dequeue()
queue.enqueue(60)
queue.print()