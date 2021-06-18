class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def addBeg(self,data):
        n = Node(data)
        if(self.head == None):
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n
        self.count+=1
            
    def addEnd(self, data):
        n = Node(data)
        if(self.head == None):
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.count+=1
        
    def delBeg(self):
        if self.head == None:
            print("List is empty.")
        elif self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
            del temp
            self.count -= 1
        else:
            temp = self.head
            self.head = temp.next
            del temp
            self.count -=1
    
    def delEnd(self):
        if(self.head == None):
            print("List is empty.")
        elif(self.head == self.tail):
            temp = self.head
            self.head = self.tail = None
            del temp
            self.count -= 1
        else:
            temp = self.head
            while(temp.next != self.tail):
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.count-=1
            
    def traversal(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end="->")
            temp = temp.next
        print("None")
            

ll = SinglyLinkedList()
ll.addBeg(100)
ll.addBeg(1000)
ll.addBeg(10)
ll.addBeg(10000)
ll.addBeg(1)
ll.delBeg()
ll.delEnd()
ll.traversal()
