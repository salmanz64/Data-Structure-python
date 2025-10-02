class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent - parent
        
    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
    
    
    def isLeaf(self):
        return not(self.rightChild or self.rightChild)
    
    def isRoot(self):
        return not self.parent
    
    def hasAnyChildren(self):
        return (self.rightChild or self.leftChild)
    
    def hasBothChildren(self):
        return (self.rightChild and self.leftChild)
    
    
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size +=1
    
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(self,key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(self,key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                
    
    def __setitem__(self,key,val):
        self.put(key,val)
        
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
            
            
    
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
        
    def __getitem__(self,key):
        return self.get(key)
    
    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False
        
    