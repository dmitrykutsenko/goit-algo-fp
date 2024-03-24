# dijkstra new

import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: {} for vertex in range(vertices)}

    def add_edge(self, source, destination, weight):
        self.adjacency_list[source][destination] = weight
        self.adjacency_list[destination][source] = weight

    def dijkstra(self, start):
        distances = [float("inf")] * self.vertices
        distances[start] = 0
        min_heap = [(0, start)]

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            for neighbor, weight in self.adjacency_list[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# Задамо граф
graph = Graph(6)
graph.add_edge(0, 1, 7)
graph.add_edge(0, 2, 9)
graph.add_edge(0, 5, 14)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 11)
graph.add_edge(2, 5, 2)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 5, 9)

start_vertex = 0
distances = graph.dijkstra(start_vertex)

for vertex, distance in enumerate(distances):
    print(f"Від вершини {start_vertex} до вершини {vertex} найкоротший шлях: {distance}")
