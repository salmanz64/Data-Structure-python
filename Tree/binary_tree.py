class BinaryTree:
    def __init__(self,val):
        self.key=val
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self,key):
        newNode = BinaryTree(key)
        if self.leftChild == None:
            self.leftChild = newNode
        else:

            newNode.leftChild = self.leftChild
            self.leftChild = newNode
    
    def insertRight(self,key):
        newNode = BinaryTree(key)
        if self.rightChild == None:
            self.rightChild = newNode
        else:

            newNode.rightChild = self.rightChild
            self.rightChild = newNode
            
    def getRoot(self):
        return self.key
    
    def setRoot(self,newVal):
        self.key = newVal
        
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild

r = BinaryTree('a')
r.insertLeft('b')            