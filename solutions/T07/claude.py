from collections import deque


def bfs(graph: dict, start) -> list:
    """Traverse graph in breadth-first order starting from start.

    Args:
        graph: Adjacency-list representation as a dict mapping each
               node to a list of its neighbours.
        start: The source node for traversal.

    Returns:
        A list of nodes in BFS visitation order.

    Time complexity: O(V + E) where V = vertices, E = edges.
    Space complexity: O(V) for the visited set and queue.
    """
    visited = {start}
    queue = deque([start])
    traversal = []
    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return traversal
