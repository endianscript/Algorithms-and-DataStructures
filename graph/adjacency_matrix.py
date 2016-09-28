import random

class DirectedGraphAM:

    def __init__(self):
        self.vertices = {}


    def add_edge(self,u,v,weight=0):
        if u not in self.vertices:
            self.vertices[u] = {}

        self.vertices[u][v] = weight

    def neighbours(self,u):
        if u in self.vertices:
            for i in self.vertices[u]:
                yield i

    def get_vertices(self):
        vertices =[]
        for u in self.vertices:
            if u not in vertices:
                vertices.append(u)
            for v in self.vertices[u]:
                if v not in vertices:
                    vertices.append(v)
        return vertices

    def get_random_vertex(self):
        vertex = self.get_vertices()
        return random.choice(vertex)

    def __repr__(self):
        rep = "graph: ["
        for u in self.vertices:
            rep += str(u) + ":"
            for v in self.vertices[u]:
                rep += '(' + str(v)
                if self.vertices[u][v]:
                    rep += ',' + str(self.vertices[u][v]) + ') '
                else:
                    rep+= '), '
        return rep + ']'

class UnDirectedGraphAM:

    def __init__(self):
        self.vertices = {}

    def add_edge(self,u,v,weight=0):
        if u not in self.vertices:
            self.vertices[u] = {}

        self.vertices[u][v] = weight

        if v not in self.vertices:
            self.vertices[v] = {}

        self.vertices[v][u] = weight

    def get_weight(self,u,v):
        return self.vertices[u][v]

    def neighbours(self,u):
        if u in self.vertices:
            for i in self.vertices[u]:
                yield i

    def get_vertices(self):
        vertices =[]
        for u in self.vertices:
            if u not in vertices:
                vertices.append(u)
            for v in self.vertices[u]:
                if v not in vertices:
                    vertices.append(v)
        return vertices


    def __repr__(self):
        rep = "graph: ["
        for u in self.vertices:
            rep += str(u) + ":"
            for v in self.vertices[u]:
                rep += '(' + str(v)
                if self.vertices[u][v]:
                    rep += ',' + str(self.vertices[u][v]) + ') '
                else:
                    rep+= '), '
        return rep + ']'


if __name__=='__main__':
    b = DirectedGraphAM(4)
    b.add_edge(0,1,5)
    b.add_edge(0,2,10)
    print(b)
    if(b.vertices[0][1]):
        print("Yes")
