from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

g = Graph()
g.addVertex('sage')
g.addVertex('a')
g.addVertex('b')
g.addEdge('sage', 'a')
g.addEdge('a', 'b')

def bfs(g: Graph, start: Vertex):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVertex = vertQueue.dequeue()
        for nbr in currentVertex.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVertex.getDistance() + 1)
                nbr.setPred(currentVertex)
                vertQueue.enqueue(nbr)
        currentVertex.setColor('black')

def traverse(y: Vertex):
    path = []
    x = y
    while x.getPred():
        path.append(x.getId())
        x = x.getPred()
    path.append(x.getId())
    print(" → ".join(reversed(path)))

# Run BFS and traverse path
bfs(g, g.getVertex('sage'))
traverse(g.getVertex('b'))  # Output: sage → a → b
