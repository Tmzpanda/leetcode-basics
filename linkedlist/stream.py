from linkedlist.utils import ListNode


class DataStream:

    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()

    def append(self, num):
        # cur
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    def remove(self, num):
        # prev
        prev = self.num_to_prev[num]
        prev.next = prev.next.next
        # cur
        del self.num_to_prev[num]   # delete dictionary
        # next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev

    def add(self, num):
        # second time
        if num in self.num_to_prev:
            self.remove(num)
        # third or above times
        if num in self.duplicates:
            return
        # first time
        self.append(num)
        self.duplicates.add(num)

    def firstUnique(self):
        if not self.dummy.next:
            return None
        return self.dummy.next.val


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.dummy = Node()
        self.tail = self.dummy
        self.key_to_prev = {}  # node.key to prev
        self.capacity = capacity

    def append(self, node):
        self.tail.next = node
        self.key_to_prev[node.key] = self.tail
        self.tail = node

    def remove(self, node):
        # prev
        prev = self.key_to_prev[node.key]
        prev.next = node.next
        # cur
        del self.key_to_prev[node.key]
        # next
        if node.next:
            self.key_to_prev[node.next.key] = prev
        else:
            self.tail = prev

    def popleft(self):
        head = self.dummy.next
        # prev
        self.dummy.next = head.next
        # cur
        del self.key_to_prev[head.key]
        # next
        if head.next:
            self.key_to_prev[head.next.key] = self.dummy
        else:
            self.tail = self.dummy

    def put(self, key, value):
        if key in self.key_to_prev:
            self.remove(self.key_to_prev[key].next)
        self.append(Node(key, value))
        if len(self.key_to_prev) > self.capacity:
            self.popleft()
        # print(self.key_to_prev)

    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        value = self.key_to_prev[key].next.value
        self.remove(self.key_to_prev[key].next)
        self.append(Node(key, value))
        return value


if __name__ == '__main__':
    stream = DataStream()
    stream.add(1)
    stream.add(2)
    print("First Unique Value is %s " % stream.firstUnique())
    stream.add(1)
    print("First Unique Value is %s " % stream.firstUnique())

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print("Value of Key 1: %s" % cache.get(1))
    cache.put(3, 3)
    print("Value of Key 2: %s" % cache.get(2))
    cache.put(4, 4)
    print("Value of Key 1: %s" % cache.get(1))
    print("Value of Key 3: %s" % cache.get(3))
    print("Value of Key 4: %s" % cache.get(4))







