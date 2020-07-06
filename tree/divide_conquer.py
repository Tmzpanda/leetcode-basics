# divide and conquer
import math

from tree.traverse import Codec


class Solution:
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


if __name__ == '__main__':

    data = "[1,-5,2,1,2,-4,-5]"
    codec = Codec()
    root = codec.deserialize(data)
    test = Solution()
    node = test.find_subtree(root)
    print("Minimum subtree root value: %s " % node.val)
