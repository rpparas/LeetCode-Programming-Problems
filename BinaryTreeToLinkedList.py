# Problem statement: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Illustration:
# Original:
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#
# First pass:
#   1
#    \
#     2
#    / \
#   3   4
#        \
#         5
#          \
#           6
#
# Second pass:
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None

            temp_right = root.right
            while temp_right.right:
                temp_right = temp_right
            temp_right.right = temp

        self.flatten(root.right)

    def print_tree(self, root):
        while root:
            print(f"{root.val}->")
            root = root.right

node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right = TreeNode(5)
node.right.right = TreeNode(6)

sol = Solution()
sol.flatten(node)
sol.print_tree(node)

