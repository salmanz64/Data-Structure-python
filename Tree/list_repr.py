def BinaryTree(r):
    return [r,[],[]]
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]],)
    else:
        root.insert(1,[newBranch,[],[]])
        
def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t) >1:
        root.insert(2,[newBranch,t,[]])
    else:
        root.insert(2,[newBranch,[],[]])

def getRoot(root):
    return root[0]

def setRoot(root,val):
    root[0]= val
    
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree('a')
insertLeft(r,'b')

insertRight(r,'c')
insertRight(getLeftChild(r),'d')
insertLeft(getRightChild(r),'e')
insertRight(getRightChild(r),'f')

print(r)

