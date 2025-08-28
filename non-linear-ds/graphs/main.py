# G = {V, E}

class DirectedGraph:
    def __init__(self):
        # Dictionary of node: list of values
        # adj = {"A": ["B", "C"]}
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")

class UndirectedGraph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    
    def print_graph(self):
        for node in self.adj_list:
            print(f"{node} - {self.adj_list[node]}")

# g = DirectedGraph()
# g.add_edge("A", "B")
# g.add_edge("B", "C")
# g.add_edge("C", "D")
# g.add_edge("D", "E")
# g.add_edge("D", "F")
# g.add_edge("E", "F")
# g.add_edge("F", "A")
# g.add_edge("F", "B")
# g.print_graph()

g = UndirectedGraph()

g.add_edge("A", "B")
g.add_edge("A", "E")
g.add_edge("A", "C")
g.add_edge("B", "E")
g.add_edge("B", "D")
g.add_edge("C", "F")
g.add_edge("C", "G")
g.add_edge("D", "E")

g.print_graph()
