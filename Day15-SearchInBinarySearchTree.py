"""
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""
from binarytree import Node


class SearchInBST:
    def searchBST(self, root, val: int):
        if root == None or root.val == val:
            return root
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


obj = SearchInBST()
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print(obj.searchBST(root, 2))