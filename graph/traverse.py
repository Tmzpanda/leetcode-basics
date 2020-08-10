from collections import deque

from graph.utils import GraphNode


def bfs_traverse(node):
    queue, visited = deque([node]), {node}
    res = []

    while queue:
        current = queue.popleft()
        res.append(current.label)

        for neighbor in current.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return res


if __name__ == '__main__':

    node1, node2, node3, node4, = GraphNode(1), GraphNode(2), GraphNode(3), GraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    print("Level order traversal of Graph: %s" % bfs_traverse(node1))







