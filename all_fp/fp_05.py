# more DFS and more BFS

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

    def draw_heap(self, traversal_type="bfs"):
        G = nx.Graph()
        positions = {}
        colors = []
        color_step = 255 // (len(self.heap) + 1)

        def add_nodes_edges(i, x, y, depth=0):
            if i < len(self.heap):
                G.add_node(self.heap[i])
                positions[self.heap[i]] = (x, y)
                # Визначення кольору для вузла
                color_value = depth * color_step  # Збільшуємо значення для отримання темнішого кольору
                color = f"#{color_value:02x}{color_value:02x}ff"  # Відтінки блакитного
                colors.append(color)
                if traversal_type == "dfs":
                    add_nodes_edges(2 * i + 1, x - 4, y - 1, depth + 1)  # Лівий нащадок
                    add_nodes_edges(2 * i + 2, x + 4, y - 1, depth + 1)  # Правий нащадок
                elif traversal_type == "bfs":
                    add_nodes_edges(2 * i + 1, x - 4, y - 1, depth + 1)  # Лівий нащадок
                    add_nodes_edges(2 * i + 2, x + 4, y - 1, depth + 1)  # Правий нащадок

        add_nodes_edges(0, 0, 0)

        edges = []
        for i in range(len(self.heap)):
            if self.parent(i) >= 0:
                edges.append((self.heap[self.parent(i)], self.heap[i]))

        G.add_edges_from(edges)

        plt.title(f"Візуалізація обходу {traversal_type.upper()}")
        labels = {node: node for node in G.nodes()}
        print(f"Кольори, що дістануться вузлам на візуалізації {traversal_type.upper()} ", colors)
        nx.draw(G, pos=positions, labels=labels, with_labels=True, node_size=1000, node_color=colors)
        plt.show()

    def dfs(self, i, visited=None):
        if visited is None:
            visited = []
        if i < len(self.heap) and i not in visited:
            visited.append(i)
            print(f"Відвідуємо вузол: {self.heap[i]}")
            self.dfs(2 * i + 1, visited)  # Лівий нащадок
            self.dfs(2 * i + 2, visited)  # Правий нащадок
        return visited

    def bfs(self):
        visited = []
        queue = [0]
        while queue:
            i = queue.pop(0)
            if i < len(self.heap) and i not in visited:
                visited.append(i)
                print(f"Відвідуємо вузол: {self.heap[i]}")
                queue.append(2 * i + 1)  # Лівий нащадок
                queue.append(2 * i + 2)  # Правий нащадок
        return visited

# Приклад купи
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

# Виконання DFS та BFS
dfs_order = heap.dfs(0)
bfs_order = heap.bfs()

print("Результат обходу в глибину (DFS):", [heap.heap[i] for i in dfs_order])
print("Результат обходу в ширину (BFS):", [heap.heap[i] for i in bfs_order])

# ВІзуалізації
heap.draw_heap("dfs")  # для DFS
heap.draw_heap("bfs")  # для BFS
