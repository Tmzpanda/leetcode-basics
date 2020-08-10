from collections import deque
from graph.utils import GraphNode
from functools import reduce

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



# Sequence Reconstruction
def sequenceReconstruction(org, seqs):

    # edge case handle
    nodes = reduce(set.union, seqs, set())      # unique elements
    if nodes != set(org):
        return False

    # graph construction
    n = len(org)
    out_edges = [[] for _ in range(n + 1)]
    in_degrees = [0 for _ in range(n + 1)]
    for seq in seqs:
        for f, t in zip(seq, seq[1:]):      # find neighbors and indegree using "zip function"
            out_edges[f].append(t)
            in_degrees[t] += 1

    # topological sorting
    queue = [node for node in org if in_degrees[node] == 0]
    order = []
    while queue:
        if len(queue) != 1:     # unique topological sorting
            return False
        node = queue.pop()
        order.append(node)
        for next_node in out_edges[node]:
            in_degrees[next_node] -= 1
            if not in_degrees[next_node]:
                queue.append(next_node)

    return org == order

# Course Schedule
# cyclic judgement


if __name__ == '__main__':
    node0, node1, node2, node3, node4, node5 = GraphNode(0), GraphNode(1), GraphNode(2), GraphNode(3), GraphNode(
        4), GraphNode(5)
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


    orgs = [1, 2, 3, 4]
    seqs = [[1, 2, 3], [1, 2, 4], [3, 4]]
    print("Sequence Reconstruction result: %s" % sequenceReconstruction(orgs, seqs))

