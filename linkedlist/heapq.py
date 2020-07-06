from heapq import *

from graph.utils import Point
from linkedlist.transform import arrayToList
from linkedlist.utils import ListNode, print_list

ListNode.__lt__ = lambda x, y: (x.val < y.val)


def mergeKLists(lists):
    dummy = ListNode(0)
    tail = dummy

    heap = []
    for node in lists:
        if node:
            heappush(heap, node)  # heapify

    while heap:
        node = heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heappush(heap, node.next)

    return dummy.next


def findKClosest(points, origin, k):
    def getDistance(a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

    heap = []
    for point in points:
        dist = getDistance(point, origin)
        heappush(heap, (-dist, -point.x, -point.y))  # default min heap
        if len(heap) > k:
            heappop(heap)

    output = []
    while len(heap) > 0:
        _, x, y = heappop(heap)
        output.append(Point(-x, -y))

    output.reverse()
    return output


if __name__ == '__main__':

    head1 = arrayToList([1, 4, 5])
    head2 = arrayToList([1, 3, 4])
    head3 = arrayToList([2])
    sorted_lists = [head1, head2, head3]
    head = mergeKLists(sorted_lists)
    print("Merge K Sorted Lists Result: ", end='')
    print_list(head)

    p1, p2, p3, p4, p5 = Point(4, 6), Point(4, 7), Point(4, 4), Point(2, 5), Point(1, 1)
    points = [p1, p2, p3, p4, p5]
    origin = Point(0, 0)
    k = 3
    result = []
    output = findKClosest(points, origin, k)
    for point in output:
        result.append((point.x, point.y))
    print("Top %s Closet Points: %s" % (k, result))
