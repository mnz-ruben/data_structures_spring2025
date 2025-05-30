#!/usr/bin/env python3
from collections import deque

def breadth_first_traverse(graph, start):
    visited = set()
    order = []
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def depth_first_traverse(graph, start):
    visited = set()
    order = []
    stack = []

    visited.add(start)
    stack.append(start)

    while stack:
        vertex = stack[-1]
        order.append(vertex)
        unvisited_found = False
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                unvisited_found = True
                break
        if not unvisited_found:
            stack.pop()
    return order

def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_vertex = 'A'
    bfs_order = breadth_first_traverse(graph, start_vertex)
    print("Breadth-First Traversal:", " -> ".join(bfs_order))

    dfs_order = depth_first_traverse(graph, start_vertex)
    print("Depth-First Traversal:", " -> ".join(dfs_order))

if __name__ == "__main__":
    main()
