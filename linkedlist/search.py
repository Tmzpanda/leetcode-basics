from linkedlist.transform import arrayToList

# middle
# fast & slow pointers
def middleNode(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

#

if __name__ == '__main__':
    array = [1, 2, 3, 4]
    arrayToList(array)
