class MinHeap:

    def __init__(self):
        self.heap = [0] # Initialize the list with 0, makes it easier for index calculation
        self.currentsize = 0
        self.node_position_map = {}

    def is_empty(self):
        return self.currentsize == 0

    def percolate_up(self, position):
        while position // 2 > 0:
            if self.heap[position] < self.heap[position // 2]:
              self.swap_node(position // 2, position)
            position = position // 2

    def swap_node(self, parent_node_position, current_node_position):
        parent_node = self.heap[parent_node_position]
        current_node = self.heap[current_node_position]
        self.node_position_map[parent_node], self.node_position_map[current_node] = self.node_position_map[current_node],self.node_position_map[parent_node]
        self.heap[parent_node_position],self.heap[current_node_position] = self.heap[current_node_position], self.heap[parent_node_position]

    def insert(self, node):
        self.heap.append(node)
        self.currentsize = self.currentsize + 1
        self.node_position_map[node] = self.currentsize
        self.percolate_up(self.currentsize)

    def get_min(self):
        return self.heap[1]

    def percolate_down(self, position):
        """
        percolate_down : Used by build_heap and extract_min functions to maintain the heap order property.
        """
        while (position * 2) <= self.currentsize: # Only non leaf nodes
            min_child_position = self.get_min_child(position)
            if self.heap[position] > self.heap[min_child_position]:
                self.swap_node(min_child_position,position)
            position = min_child_position

    def get_min_child(self, position):
        """
        get_min_child : Helper function for percolate down
        :param position: The position of the parent node
        :return: Position of the child with the minimum value
        """
        if (position * 2 + 1) > self.currentsize: # Check if right node exists, if not return the left node
            return position * 2
        else:
            if self.heap[position * 2] < self.heap[position * 2 + 1]:
                return position * 2
            else:
                return position * 2 + 1

    def extract_min(self):
        minval = self.heap[1]
        self.heap[1] = self.heap[self.currentsize]
        self.heap.pop()
        self.currentsize = self.currentsize - 1
        self.percolate_down(1)
        return minval

    def decrease_key(self, node, value):
        if node in self.node_position_map:
            position = self.node_position_map[node]
            del self.node_position_map[node]
            self.heap[position] = value
            self.percolate_up(position)

    def build_heap(self, key_list):
        """
        Inserting one key at a time would result in a complexity of O(n lg n)
            O(log n) for each binary search operation in order to insert the key in the right location
        Hence, we insert the entire list that would result in a complexity of O(n)

        :param key_list: List containing keys which need to be constructed as a Heap
        """
        self.currentsize = len(key_list)
        self.heap = [0] + key_list[:] # Reinitialize the heap with the given key_list
        position = len(key_list) // 2 # Gives us the last non leaf node in the list
        while (position > 0):         # From the last non leaf node, continue to percolate down by moving upwards.
            self.percolate_down(position)
            position = position - 1

    def __repr__(self):
        heap = [item for i, item in enumerate(self.heap) if i > 0]
        return "Heap: " + str(heap)

    def __contains__(self, item):
        return True if item in self.node_position_map else False

    def __getitem__(self, item):
        position = self.node_position_map[item]
        return self.heap[position]

if __name__ == '__main__':
   pass