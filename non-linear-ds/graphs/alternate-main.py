class Vertex:
    def __init__(self, data):
        self.data = data
        self.edge_to = []

    def __repr__(self):
        return self.data
    
class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, source, next):
        if source not in self.vertices:
            self.vertices.append(source)
        source.edge_to.append(next)
    
    def print_graph(self):
        for vertex in self.vertices:
            print(f"{vertex} -> {vertex.edge_to}")
        

    
# creating vertices
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")

g = Graph()

g.add_vertex(a, b)
g.add_vertex(a, c)
g.add_vertex(b, c)
g.add_vertex(c, a)

g.print_graph()