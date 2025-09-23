# This is an unordered list so many features like append,insert can be implemented 


#Node representation of Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.nextNode
    
    def setData(self,newData):
        self.data = newData
        
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.nextNode
        return " -> ".join(values) if values else "Empty List"

        
    def isEmpty(self):
        return self.head == None
    
    def add(self,data):
        newNode = Node(data)
        newNode.nextNode = self.head
        self.head = newNode
        
    def size(self):
        count = 0
        current = self.head
        while current !=None:
            count+=1
            current = current.getNext()
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current!=None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    def remove(self,item):
        current = self.head
        prev = None
        found= False
        while not found:
            if current.getData() == item:
                found = True
            else:
                prev= current
                current = current.getNext()
        if prev == None:
            self.head = self.head.getNext()
        else:
            prev.nextNode = current.getNext()
            
    def append(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.nextNode != None:
                current = current.nextNode
        
            current.nextNode = newNode
            
    def insert(self,item,pos):
        newNode = Node(item)
        index =0
        current = self.head
        prev = None
        while current != None:
            if pos == index:
                break
            else:
                prev = current
                current = current.nextNode
            index +=1
        if prev == None:
            newNode.nextNode = self.head
            self.head = newNode
        else:
            prev.nextNode = newNode
            newNode.nextNode = current
            
    def index(self,item):
        current = self.head
        index = 0
        while current!=None:
            if current.getData() == item:
                break
            else:
                current = current.nextNode
            index+=1
        return index
    def pop(self,pos):
        index = 0
        current = self.head
        prev = None
        while current != None:
            if pos == index:
                break
            else:
                prev = current
                current = current.nextNode
            index+=1
        if prev == None:
            self.head = self.head.nextNode
        else:
            prev.nextNode = current.nextNode
        return current.getData()
                

     
mylist = SingleLinkedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))

mylist.insert(20,0)
mylist.insert(10,1)
print(mylist.search(10))
print(mylist.search(20))
print(mylist.index(10))
print(mylist)
                
    
    
                
    
        
        
        