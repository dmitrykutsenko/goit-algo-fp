# pyramid visualization

import networkx as nx
import matplotlib.pyplot as plt

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def draw_heap(self):
        G = nx.Graph()
        positions = {}

        def add_nodes_edges(i, x, y):
            if i < len(self.heap):
                G.add_node(i, weight=self.heap[i])
                positions[i] = (x, y)
                add_nodes_edges(2 * i + 1, x - 4, y - 1)  # Лівий нащадок
                add_nodes_edges(2 * i + 2, x + 4, y - 1)  # Правий нащадок

        add_nodes_edges(0, 0, 0)

        edges = []
        for i in range(len(self.heap)):
            if self.parent(i) >= 0:
                edges.append((self.parent(i), i))

        G.add_edges_from(edges)

        weights = nx.get_node_attributes(G, 'weight')
        nx.draw(G, pos=positions, labels=weights, with_labels=True, node_size=1000, node_color='skyblue')
        plt.show()


# Приклад використання
heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(2)
heap.insert(7)
heap.insert(6) 
heap.insert(9)  
heap.insert(4)  
heap.insert(1)  
heap.draw_heap()
