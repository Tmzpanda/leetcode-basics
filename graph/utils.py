class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []


class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b


matrix1 = [[1, 1, 0, 0, 0],
           [0, 1, 0, 0, 1],
           [0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1]]
matrix2 = [[0, 1, 0],
           [0, 0, 1],
           [0, 0, 0]]



