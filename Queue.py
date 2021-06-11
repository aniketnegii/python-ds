class Queue:
    
    def __init__(self, maxSize):
        self.front = 0
        self.rear = -1
        self.maxSize = maxSize
        self.l = [None for i in range(maxSize)]

    def empty(self) :
        if (self.rear - self.front +1 ) == 0:
            return True
        else:
            False
    
    def full(self) :
        if self.rear == self.maxSize -1 :
            return True
        else:
            return False
    
    def Dequeue(self) :
        if(self.empty()):
            print("Queue empty.")
        else:
            x = self.l[self.front]
            self.l[self.front] = None
            self.front = self.front + 1
            return x
    
    def Enqueue(self, val) :
        if(self.full()):
            print("Stack is full")
        else:
            self.rear = self.rear + 1
            self.l[self.rear] = val
            
    def display(self):
        for i in range(self.front, self.rear+1):
            print(self.l[i], end=" ")
        print()

s1 = Queue(10)
s1.Dequeue()

for i in range(10):
    s1.Enqueue(i)

print("Current Queue:", end=" ")
s1.display()

print("Deleted values: ", end=" ")
for i in range(4):
    x = s1.Dequeue()
    print(x, end=" ")
print()
    
print("Current Queue(after deletion):", end=" ")
s1.display()