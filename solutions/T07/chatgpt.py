from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    visited.add(start)
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result
