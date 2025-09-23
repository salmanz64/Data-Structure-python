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
        
        
class OrderedList:
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
        
        current = self.head
        prev = None
        stop = False
        
        while current != None and not stop:
            if current.getData() > data:
                stop = True
            else:
                prev = current
                current = current.nextNode
        if prev == None:
            newNode.nextNode = self.head
            self.head = newNode
        else:
            prev.nextNode = newNode
            newNode.nextNode = current
        
        
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
        stop = False
        while current!=None and not found:
            if current.getData() == item:
                found = True
            else:
                if current.getData()>item:
                    return  False
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
                



mylist = OrderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist)

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

print(mylist.index(10))
print(mylist)

                
    
    
                
    
        
        
        