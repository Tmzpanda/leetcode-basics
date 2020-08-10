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


# Graph Paths From Source to Target
# DFS
class Solution:

    def allPathsSourceTarget(self, graph):
        paths = []
        self.dfs(graph, 0, len(graph) - 1, [0], paths)

        return paths

    def dfs(self, graph, node, target, path, paths):
        if node == target:
            paths.append(path[:])   # deep copy
            return

        for next_node in graph[node]:
            path.append(next_node)
            self.dfs(graph, next_node, target, path, paths)
            path.pop()


if __name__ == '__main__':

    node1, node2, node3, node4, = GraphNode(1), GraphNode(2), GraphNode(3), GraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    print("Level order traversal of Graph: %s" % bfs_traverse(node1))







