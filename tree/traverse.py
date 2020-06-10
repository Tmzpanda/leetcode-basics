from tree.codec import Codec, draw_tree

root = Codec.deserialize("[1,2,3,#,#,4,5]")
draw_tree(root)

