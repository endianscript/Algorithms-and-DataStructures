from heap.min_heap import MinHeap
from graph.adjacency_matrix import UnDirectedGraphAM
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


def dijkstras_algorithm(graph):
    heap = MinHeapNode()

    vertex_distance_map = {}
    vertex_path_map = {}

    for vertex in graph.get_vertices():
        heap.insert(HeapNode(vertex,sys.maxsize))

    heap.decrease_key('A',0)
    vertex_distance_map['A'] = 0
    vertex_path_map['A'] = None

    while not heap.is_empty():
        current_vertex = heap.extract_min()
        for next_vertex in graph.neighbours(current_vertex.key):
            if next_vertex in heap:
                new_cost = vertex_distance_map[current_vertex.key] + graph.get_weight(current_vertex.key,next_vertex)
                current_cost = heap[next_vertex].get_value()
                if new_cost < current_cost:
                    vertex_distance_map[next_vertex] = new_cost
                    vertex_path_map[next_vertex] = current_vertex.key
                    heap.decrease_key(next_vertex,new_cost)

    print(vertex_path_map)
    print(vertex_distance_map)


if __name__=='__main__':
    graph = UnDirectedGraphAM()

    graph.add_edge('A','B',5)
    graph.add_edge('A','E',2)
    graph.add_edge('E','F',3)
    graph.add_edge('A','D',9)
    graph.add_edge('F','D',2)
    graph.add_edge('D','C',3)
    graph.add_edge('B','C',2)

    dijkstras_algorithm(graph)
