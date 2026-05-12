from collections import deque


def bfs(graph, start):
    visited = []
    queue = deque()
    queue.append(start)
    seen = set()
    seen.add(start)
    while queue:
        current = queue.popleft()
        visited.append(current)
        for neighbor in graph.get(current, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return visited
