from collections import deque


class Codec:

    @staticmethod
    def serialize(root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
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

        return "[%s]" % ','.join(bfs_order)  # "[1,2,3,#,#,4,5]"

    @staticmethod
    def deserialize(data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == "[]":
            return None

        vals = data[1:-1].split(',')    # ['1', '2', '3', '#', '#', '5']
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


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def draw_tree(root):

    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jump_to(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jump_to(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jump_to(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)

    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jump_to(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()


def main():
    data = "[1,2,3,#,#,4,5]"
    root = Codec.deserialize(data)
    draw_tree(root)


if __name__ == '__main__':
    main()
