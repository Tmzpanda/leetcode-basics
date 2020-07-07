# divide and conquer
import math

from tree.traverse import Codec


# Minimum Subtree
from tree.utils import TreeNode, draw_tree


# Minimum Subtree
class Solution1:
    def __init__(self):
        self.minimum = math.inf
        self.subtree = None

    def find_subtree(self, root):
        self.rec(root)
        return self.subtree

    def rec(self, root):
        if root is None:
            return 0

        left_sum = self.rec(root.left)
        right_sum = self.rec(root.right)
        root_sum = left_sum + right_sum + root.val
        if root_sum < self.minimum:
            self.minimum = root_sum
            self.subtree = root

        return root_sum


# Lowest Common Ancestor
def lowestCommonAncestor(root, A, B):
    if root is None:
        return None
    if root is A or root is B:
        return root

    left = lowestCommonAncestor(root.left, A, B)
    right = lowestCommonAncestor(root.right, A, B)
    if left is not None and right is not None:
        return root
    if left is not None:
        return left
    if right is not None:
        return right
    return None


# LCA does not exist situation
class Solution2:
    def lowestCommonAncestor(self, root, A, B):
        a, b, node = self.rec(root, A, B)
        if a and b:
            return node
        return None

    def rec(self, root, A, B):
        if root is None:
            return False, False, None

        left_a, left_b, left_node = self.rec(root.left, A, B)
        right_a, right_b, right_node = self.rec(root.right, A, B)
        a = left_a or right_a or root == A
        b = left_b or right_b or root == B
        if root == A or root == B:
            return a, b, root
        if left_node is not None and right_node is not None:
            return a, b, root
        if left_node is not None:
            return a, b, left_node
        if right_node is not None:
            return a, b, right_node
        return a, b, None


# LCA in BST
def lowestCommonAncestorInBST(root, p, q):
    parent_val, p_val, q_val = root.val, p.val, q.val

    if p_val > parent_val and q_val > parent_val:
        return lowestCommonAncestor(root.right, p, q)
    elif p_val < parent_val and q_val < parent_val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return root


if __name__ == '__main__':

    data = "[1,-5,2,1,2,-4,-5]"
    codec = Codec()
    root = codec.deserialize(data)
    test = Solution1()
    node = test.find_subtree(root)
    print("Minimum subtree root value: %s " % node.val)

    node1, node2, node3, node4, node5 = TreeNode(4), TreeNode(3), TreeNode(7), TreeNode(5), TreeNode(8)
    node1.left, node1.right = node2, node3
    node3.left, node3.right = node4, node5
    # draw_tree(node1)
    node = lowestCommonAncestor(node1, node2, node5)
    print("Lowest Common Ancestor Value: %s" % node.val)

    node6 = TreeNode(100)
    test = Solution2()
    node = test.lowestCommonAncestor(node1, node3, node6)
    value = node.val if node is not None else None
    print("Lowest Common Ancestor Value: %s" % value)

    node = lowestCommonAncestorInBST(node1, node2, node4)
    print("Lowest Common Ancestor Value in a BST: %s" % node.val)


