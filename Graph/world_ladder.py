
class Vertex:
    def __init__(self,key):
        self.key = key
        self.connectedTo = {}
        
    def addNeighbour(self,nbr,weight = 0):
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        return str(self.key) + 'connected to ' + str([x.key for x in self.connectedTo])
    
    def getConnection(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.key
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numOfVertices = 0
        
    def addVertex(self,key):
        v = Vertex(key)
        self.vertList[key] = v
        self.numOfVertices+=1
        return v
    
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def addEdge(self,f,v,weight = 0):
        if f not in self.vertList:
            fromV = self.addVertex(f)
        if v not in self.vertList:
            toV = self.addVertex(v)
        
        self.vertList[f].addNeighbour(self.vertList[v],weight)
    
    def getVertices(self,key):
        return self.vertList.keys()
    
    def __iter__(self):
      return iter(self.vertList.values())

         
 

def buildGraph(self):
    d= {}
    g = Graph()
    
    wfile = open(wordFile.txt,'r')
    
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)