from functools import reduce


# unique elements in a series of lists
seqs = [[1, 2, 3], [1, 2, 4], [3, 4]]
nodes = reduce(set.union, seqs, set())
print(nodes)

