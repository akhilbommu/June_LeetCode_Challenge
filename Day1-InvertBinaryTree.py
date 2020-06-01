"""
https://leetcode.com/problems/invert-binary-tree/
"""

from binarytree import Node


class InvertBinaryTree:

    def invertTree(self, root):
        if not root:
            return None
        right, left = self.invertTree(root.right), self.invertTree(root.left)
        root.left, root.right = right, left
        return root


obj = InvertBinaryTree()
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(9)

print('Binary Tree :', root)  # Getting binary tree
print('Inverted Binary Tree :', obj.invertTree(root))
