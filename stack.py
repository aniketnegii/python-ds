class Stack:
    
    def __init__(self, maxSize):
        self.top = -1
        self.maxSize = maxSize
        self.l = [None for i in range(maxSize)]

    def empty(self) :
        if self.top == -1:
            return True
        else:
            False
    
    def full(self) :
        if self.top == self.maxSize -1 :
            return True
        else:
            return False
            
    def peek(self) :
        return self.l[self.top]
    
    def Pop(self) :
        if(self.empty()):
            print("Stack empty.")
        else:
            x = self.l.pop(self.top)
            self.top = self.top -1
            return x
    
    def Push(self, val) :
        if(self.full()):
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.l[self.top] = val
            
    def display(self):
        for i in range(self.top+1):
            print(self.l[i], end=" ")
        print()

s1 = Stack(10)
s1.Pop()
for i in range(10):
    s1.Push(i)
s1.display()
a = s1.Pop()
s1.display()
print(a)
print(s1.peek())