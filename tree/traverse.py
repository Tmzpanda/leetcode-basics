from collections import deque
from tree.utils import draw_tree, TreeNode


def preorder_traverse(root):
    result = []

    def rec(node):
        if node is None:
            return
        result.append(node.val)
        rec(node.left)
        rec(node.right)

    rec(root)
    print("preorder traversal: %s " % result)
    return result


def inorder_traverse(root):     # bst non-decreasing order
    result = []

    def rec(node):
        if node is None:
            return
        rec(node.left)
        result.append(node.val)
        rec(node.right)

    rec(root)
    print("inorder traversal: %s " % result)
    return result


def postorder_traverse(root):      # delete binary tree
    result = []

    def rec(node):
        if node is None:
            return
        rec(node.left)
        rec(node.right)
        result.append(node.val)

    rec(root)
    print("postorder traversal: %s " % result)
    return result


def find_path(root):
    result, path = [], [str(root.val)]

    def rec(node):
        if node.left is None and node.right is None:
            result.append('->'.join(path))

        if node.left:
            path.append(str(node.left.val))
            rec(node.left)
            path.pop()
        if node.right:
            path.append(str(node.right.val))
            rec(node.right)
            path.pop()

    rec(root)
    return result


def bfs_traverse(root):
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    print("level order traversal: %s" % result)
    return result


class Codec:

    @staticmethod
    def serialize(root):
        if root is None:
            return ""

        # use bfs to serialize the tree
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)

        while bfs_order[-1] == '#':
            bfs_order.pop()

        return "[%s]" % ','.join(bfs_order)  # "[8,3,10,1,6,#,14,#,#,4,7,13]"

    @staticmethod
    def deserialize(data):

        if data == "[]":
            return None

        vals = data[1:-1].split(',')  # ['8', '3', '10', '1', '6', '#', '14', '#', '#', '4', '7', '13']
        root = TreeNode(int(vals[0]))
        queue = [root]
        index = 0
        is_left_child = True

        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if is_left_child:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not is_left_child:
                index += 1

            is_left_child = not is_left_child

        return root


if __name__ == '__main__':
    data = "[8,3,10,1,6,#,14,#,#,4,7,13]"
    codec = Codec()
    root = codec.deserialize(data)
    # draw_tree(root)

    preorder_traverse(root)
    inorder_traverse(root)
    postorder_traverse(root)

    root = codec.deserialize("[1,2,3,#,5]")
    print("All possible paths: %s" % find_path(root))

    bfs_traverse(root)
    data = "[8,3,10,1,6,#,14,#,#,4,7,13]"
    codec = Codec()
    root = codec.deserialize(data)
    # draw_tree(root)
    print("Serialization output: %s" % codec.serialize(root))
