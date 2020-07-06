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



































#
# class LinkedList:
#     def __init__(self, arr):
#         return


# def delete_node(root, val):
    #
    #
    #
    #     def search_parent(parent, root, val):
    #         if not root:
    #             return None
    #         if root.val == val:
    #             return parent
    #         if root.val < val:
    #             return search_parent(root, root.left, val)
    #         else:
    #             return search_parent(root, root.left, val)

    #     def delete(parent, node):
    #
    #         # leaf node：直接删除 并修改parent node指针
    #         # 单枝节点：删除链表操作
    #
    #         # 没有右
    #         if not node.right:
    #             if parent.left == node:
    #                 parent.left = node.left
    #             else:
    #                 parent.right = node.left
    #
    #         # 双枝节点：与左子树最大或右子树最小交换 再删除待删叶子节点
    #
    #         # 有右
    #         else:
    #             temp = node.right
    #             father = node
    #             # 右子树最小
    #             # 右节点的左子树
    #             while temp.left:
    #                 father = temp
    #                 temp = temp.left
    #             if father.left == temp:
    #                 father.left = temp.right
    #             # 右节点的右子树
    #             else:
    #                 father.right = temp.right
    #
    #             # 左节点
    #             if parent.left == node:
    #                 parent.left = temp
    #             else:
    #                 parent.right = temp
    #             temp.left = node.left
    #             temp.right = node.right
    #
    #         return
    #
    #
    #     dummy = ListNode(10086)
    #     dummy.next = root
    #     parent = search_parent(dummy, root, val)
    #     node = None
    #
    #     if parent.left and parent.left.val == val:
    #         node = parent.left
    #     elif parent.right and parent.right.val == val:
    #         node = parent.right
    #
    #     delete(parent, node)
    #     return dummy.next
    #
    # # case1: no child
    # # case2: 1 child