from linkedlist.utils import ListNode, print_list


def arrayToList(array):
    dummy = ListNode(0)
    cur = dummy
    for num in array:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next


# merge
def mergeTwoLists(l1, l2):      # O(1) extra space
    temp = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next

    if l1 is not None:
        temp.next = l1
    else:
        temp.next = l2
    return dummy.next


def mergeKLists(lists):

    def mergeRange(lists, start, end):
        if start >= end:
            return lists[start]

        mid = (start + end) // 2
        left = mergeRange(lists, start, mid)
        right = mergeRange(lists, mid + 1, end)
        return mergeTwoLists(left, right)

    return mergeRange(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    head1 = arrayToList([1, 2, 4])
    print_list(head1)
    head2 = arrayToList([1, 5, 6])
    print_list(head2)
    head3 = arrayToList([3, 4, 7])
    print_list(head3)

    # head = mergeTwoLists(head1, head2)
    # print("Merge 2 Sorted Lists Result: ", end='')
    # print_list(head)

    head = mergeKLists([head1, head2, head3])
    print("Merge K Sorted Lists Result: ", end='')
    print_list(head)
