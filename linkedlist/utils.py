class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print('->'.join(result))
