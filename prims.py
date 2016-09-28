from graph import adjacency_matrix
from heap.min_heap import MinHeap
import sys

class HeapNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __repr__(self):
        return "(" + str(self.key) +"," + str(self.value) +")"

class MinHeapNode(MinHeap):

    def insert(self,node):
        self.heap.append(node)
        self.currentsize = self.currentsize + 1
        self.node_position_map[node.key] = self.currentsize
        self.percolate_up(self.currentsize)

    def extract_min(self):
        minval = self.heap[1]
        del self.node_position_map[minval.key]
        self.heap[1] = self.heap[self.currentsize]
        self.node_position_map[self.heap[1].key] = 1
        self.heap.pop()
        self.currentsize = self.currentsize - 1
        self.percolate_down(1)
        return minval

    def decrease_key(self, key, value):
        if key in self.node_position_map:
            position = self.node_position_map[key]
            self.heap[position] = HeapNode(key,value)
            self.percolate_up(position)

    def swap_node(self, parent_node_position, current_node_position):
        parent_node = self.heap[parent_node_position]
        current_node = self.heap[current_node_position]
        self.node_position_map[parent_node.key] = current_node_position
        self.node_position_map[current_node.key] = parent_node_position
        self.heap[parent_node_position],self.heap[current_node_position] = self.heap[current_node_position], self.heap[parent_node_position]

def prims_algorithm(graph):
    heap = MinHeapNode()
    vertex_edge_map = {}
    result = []

    for vertex in graph.get_vertices():
        heap.insert(HeapNode(vertex,sys.maxsize))

    heap.decrease_key('A', 0)

    while not heap.is_empty():
        current_vertex = heap.extract_min()
        if current_vertex.key in vertex_edge_map:
            result.append(vertex_edge_map[current_vertex.key])

        for next_vertex in graph.neighbours(current_vertex.key):
            if next_vertex in heap:
                new_weight = graph.get_weight(current_vertex.key,next_vertex)
                cost = heap[next_vertex].get_value()
                if new_weight < cost:
                    heap.decrease_key(next_vertex,new_weight)
                    vertex_edge_map[next_vertex] = (current_vertex.key,next_vertex)

    return result

def djikstras_algorithm(graph):
    heap = MinHeapNode()

    vertex_distance_map = {}
    vertex_path_map = {}

    for vertex in graph.get_vertices():
        heap.insert(HeapNode(vertex,sys.maxsize))

    heap.decrease_key('A',0)
    vertex_distance_map['A']=0
    vertex_path_map['A']=None


if __name__=='__main__':

    # TestCase
    graph = adjacency_matrix.UnDirectedGraphAM()


    graph.add_edge('A','D',1)
    graph.add_edge('A','B',3)
    graph.add_edge('B','D',3)
    graph.add_edge('B','C',1)
    graph.add_edge('C','D',1)
    graph.add_edge('D','E',6)
    graph.add_edge('C','E',5)
    graph.add_edge('E','F',2)


    print(prims_algorithm(graph))




