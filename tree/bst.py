from collections import deque

from tree.traverse import bfs_traverse
from tree.utils import draw_tree, TreeNode


def sorted_array_to_bst(nums):
    def rec(nums, start, end):  # divide and conquer paradigm
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = rec(nums, start, mid - 1)
        root.right = rec(nums, mid + 1, end)
        return root

    return rec(nums, 0, len(nums) - 1)


def insert_node(root, node):
    if not root:
        return node
    if root.val > node.val:
        root.left = insert_node(root.left, node)
    else:
        root.right = insert_node(root.right, node)
    return root


def delete_node(root, val):
    if not root:
        return

    if root.val > val:
        root.left = delete_node(root.left, val)
    elif root.val < val:
        root.right = delete_node(root.right, val)

    else:
        #  No Child or One Child
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        # Two children -> Find min node in right-subtree, copy the value, delete min node from right-subtree
        else:
            temp = find_smallest(root.right)
            root.val = temp.val
            root.right = delete_node(root.right, temp.val)
    return root


def update_node(root, val, target):
    if not root:
        return
    if val < root.val:
        root.left = update_node(root.left, val, target)
    elif val > root.val:
        root.right = update_node(root.right, val, target)
    else:
        root.val = target
    return root


def find_smallest(root):
    while root.left:
        root = root.left
    return root


# inorder traversal iteration version
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        res = node

        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return res


def find_kth_smallest(root, k):
    stack = []
    while root:
        stack.append(root)
        root = root.left

    for i in range(k):
        node = stack.pop()
        res = node

        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left

    return res.val


def find_closet(root, target):
    upper, lower = None, None
    while root:
        if target > root.val:
            lower = root
            root = root.right
        elif target < root.val:
            upper = root
            root = root.left
        else:
            return root.val

    if abs(upper.val - target) <= abs(lower.val - target):
        return upper.val
    return lower.val


def find_k_closest_recursion(root, target, k):
    res = deque()

    def rec(root):
        if root is None:
            return
        rec(root.left)
        if len(res) == k:
            if not abs(target - root.val) < abs(target - res[0]):
                return
            res.popleft()
        res.append(root.val)
        rec(root.right)

    rec(root)
    return res


# find k closest iteration
class Solution:
    def find_k_closest(self, root, target, k):  # quick select
        if root is None or k == 0:
            return []

        upper = self.find_upper_closest(root, target)
        upper_stack = [upper]
        lower = self.find_prev(upper)
        lower_stack = [lower]

        result = []
        for i in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                result.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                result.append(upper_stack[-1].val)
                self.move_upper(upper_stack)

        return result

    @staticmethod
    def find_prev(node):
        if node.left:
            node = node.left
            while node.right:
                node = node.right
        return node

    @staticmethod
    def find_upper_closest(root, target):
        upper, lower = None, None
        while root:
            if target > root.val:
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root
        return upper

    @staticmethod
    def move_upper(stack):
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left

    @staticmethod
    def move_lower(stack):
        node = stack.pop()
        if node.left:
            node = node.left
            while node:
                stack.append(node)
                node = node.right

    @staticmethod
    def is_lower_closer(lower_stack, upper_stack, target):
        if not lower_stack:
            return False
        if not upper_stack:
            return True
        return target - lower_stack[-1].val <= upper_stack[-1].val - target


if __name__ == '__main__':

    nums = [1, 3, 4, 6, 7, 8, 10, 13, 14]
    root = sorted_array_to_bst(nums)
    print("Level order traversal for root: %s " % bfs_traverse(root))

    root2 = insert_node(root, TreeNode(15))
    print("Level order traversal for root2: %s " % bfs_traverse(root2))
    # draw_tree(root2)

    root3 = delete_node(root2, 10)
    print("Level order traversal for root3: %s " % bfs_traverse(root3))
    # draw_tree(root3)

    root4 = update_node(root3, 15, 16)
    print("Level order traversal for root4: %s " % bfs_traverse(root4))

    node = find_smallest(root4)
    print("Smallest node value in root: %s" % node.val)

    res = []
    obj = BSTIterator(root4)
    while obj.hasNext():
        node = obj.next()
        res.append(node.val)
    print("Inorder traversal iteration: %s" % res)

    val = find_kth_smallest(root4, 2)
    print("Kth smallest node value in root: %s" % val)

    val = find_closet(root4, 11)
    print("Closest node value to 11: %s" % val)

    res = find_k_closest_recursion(root4, 11, 3)
    print("K closest node value to 11: %s " % res)

    test = Solution()
    res = test.find_k_closest(root4, 11, 3)
    print("K closest node value to 11: %s " % res)
