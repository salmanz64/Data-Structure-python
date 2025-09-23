class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def hashFunction(self,key):
        return key% self.size
    
    def rehashing(self,oldkey):
        return (oldkey+1)%self.size
    
    def put(self,key,data):
        hashValue = self.hashFunction(key)
        
        if self.slots[hashValue]==None:
            self.slots[hashValue] = key
            self.data[hashValue]= data
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                nextslots = self.rehashing(hashValue)
                while self.slots[nextslots]!=None and self.slots[nextslots]!=key:
                    nextslots = self.rehashing(nextslots)
                if self.slots[nextslots] == None:
                    self.slots[nextslots] = key
                    self.data[nextslots] = data
                else:
                    self.data[nextslots] = data
            
    def get(self,key):
        startSlot = self.hashFunction(key)
        data = None
        stop = False
        found = False
        
        position = startSlot
        while self.slots[position] != None and not found and not stop:
            if position == self.slots[position]:
                data = self.data[data]
                found = True
            else:
                position = self.rehashing(key)
                if(position == startSlot):
                    stop = True
        return data
    
    def __setitem__(self, name, value):
        self.put(name,value)
    
    def __getitem__(self, name):
        self.get(name)
        

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])
