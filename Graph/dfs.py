from pythonds.graphs import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
        
    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
            
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsVisit(aVertex)
                
    def dfsVisit(self,aVertex):
        aVertex.setColor('grey')
        self.time+=1
        aVertex.setDiscovery(self.time)
        
        for neighbourV in aVertex.getConnections():
            if neighbourV.getColor() =='white':
                neighbourV.setPred(aVertex)
                self.dfsVisit(neighbourV)
        aVertex.setColor('black')
        self.time+=1
        aVertex.setFinish(self.time)
            
                