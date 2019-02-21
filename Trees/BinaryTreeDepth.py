# Problem Statement: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


try: 
    s = Solution()
    tree = TreeNode(None)
    assert s.maxDepth(tree) == 1

    tree = TreeNode(3)
    tree.left = TreeNode(9)
    assert s.maxDepth(tree) == 2

    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    assert s.maxDepth(tree) == 3

    print("Yay! Test Cases Passed")    
except:
    print("Oops! Test Cases Failed")    
