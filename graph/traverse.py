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


# topological sorting
# DAG
def topSort(graph):
    node_to_indegree = get_indegree(graph)
    start_nodes = [n for n in graph if node_to_indegree[n] == 0]
    queue = deque(start_nodes)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in node.neighbors:
            node_to_indegree[neighbor] -= 1
            if node_to_indegree[neighbor] == 0:
                queue.append(neighbor)

    return result


def get_indegree(graph):
    node_to_indegree = {x: 0 for x in graph}
    for node in graph:
        for neighbor in node.neighbors:
            node_to_indegree[neighbor] += 1
    return node_to_indegree


if __name__ == '__main__':

    node1, node2, node3, node4, = GraphNode(1), GraphNode(2), GraphNode(3), GraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    print("Level order traversal of Graph: %s" % bfs_traverse(node1))

    node0, node1, node2, node3, node4, node5 = GraphNode(0), GraphNode(1), GraphNode(2), GraphNode(3), GraphNode(4), GraphNode(5)
    node0.neighbors = [node1, node2, node3]
    node1.neighbors = [node4]
    node2.neighbors = [node4, node5]
    node3.neighbors = [node4, node5]
    graph = [node0, node1, node2, node3, node4, node5]
    result = topSort(graph)
    values = []
    for node in result:
        values.append(node.label)
    print("Topological Sorting result: %s" % values)





