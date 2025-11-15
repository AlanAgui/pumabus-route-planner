class Graph:
    def __init__(self):
        self.list_adj = {}
    
    def agregarNodo(self, nodo):
        if nodo not in self.list_adj:
            self.list_adj[nodo] = []

    def agregarArista(self, u, v, weight=1):
        self.agregarNodo(u)
        self.agregarNodo(v)
        self.list_adj[u].append((v,weight))

    # Hacemos que sea directed graph
    def make_it_directed(self, u, v, weight=1):
        self.agregarArista(u, v, weight)
        self.agregarArista(v, u, weight)
    