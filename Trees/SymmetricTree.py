# Problem Statement: https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.isSymmetricHelper(root.left, root.right)


    def isSymmetricHelper(self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        return left.val == right.val and self.isSymmetricHelper(left.right, right.left) and self.isSymmetricHelper(right.right, left.left)


# Test Cases
try:
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right = TreeNode(1)

    sol = Solution()
    assert sol.isSymmetric(tree) == False

    tree = TreeNode(5)
    tree.left = TreeNode(1)
    tree.right = TreeNode(1)
    tree.left.left = TreeNode(-3)
    tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(2)
    tree.right.right = TreeNode(-3)

    assert sol.isSymmetric(tree) == True

    print("All test cases passed. Yay!")
except AssertionError:
    print("At least 1 test case failed. Check!")
finally:
    print("End of testing " + str(sol.__class__))