class BinHeap:
    def __init__(self):
        self.heap =[0]
        self.current_size = 0
        
    def percUp(self,i):
        while i // 2>0:
            if self.heap[i] < self.heap[i//2]:
                temp = self.heap[i//2]
                self.heap[i //2] = self.heap[i]
                self.heap[i] = temp
            i = i // 2
            
    def insert(self,val):
        self.heap.append(val)
        self.current_size +=1
        self.percUp(self.current_size)
    
    def percDown(self,i):
        while (i * 2) <= self.current_size:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                temp = self.heap[mc]
                self.heap[mc] = self.heap[i]
                self.heap[i] = temp
            i = mc
            
    def minChild(self,i):
        if i * 2 +1 >self.current_size:
            return i *2
        else:
            if self.heap[i*2] < self.heap[i*2 +1]:
                return i *2
            else:
                return i * 2 +1
            
    def delMin(self):
        retVal = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.current_size -=1
        self.heap.pop()
        self.percDown(1)
        return retVal
    
    def buildHeap(self,alist):
      i = len(alist) // 2
      self.current_size = len(alist)
      self.heap = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
          
bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
       
                
                
        