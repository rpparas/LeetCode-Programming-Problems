# Problem Statement: https://leetcode.com/problems/path-sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def has_path_sum(self, root: 'TreeNode', target: 'int') -> 'int':
        if root is None:
            return False
            # some people might consider the absence of a node as summing to zero
            # (need to verify how to handle that edge case)
            # return target == 0

        return self.has_path_sum_helper(root, target, 0)


    def has_path_sum_helper(self, root, target, running_total):
        running_total += root.val

        if running_total == target and root.left is None and root.right is None:
            return True

        if root.left:
            path_in_left = self.has_path_sum_helper(root.left, target, running_total)
            if path_in_left:
                return True

        if root.right:
            path_in_right = self.has_path_sum_helper(root.right, target, running_total)
            if path_in_right:
                return True

        return False


# Test cases:
try:
    s = Solution()
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right = TreeNode(8)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right = TreeNode(1)
    assert s.has_path_sum(tree, 5) == False
    assert s.has_path_sum(tree, 13) == False
    assert s.has_path_sum(tree, 22) == True

    tree = TreeNode(0)
    assert s.has_path_sum(tree, 0) == True

    tree.right = TreeNode(8)
    assert s.has_path_sum(tree, 0) == False

    tree.left = TreeNode(-1)
    tree.left.left = TreeNode(-3)
    assert s.has_path_sum(tree, -4) == True

    tree = None
    assert s.has_path_sum(tree, 0) == False # see comment above lines 13-16

    print("All test cases passed. Yay!")
except AssertionError:
    print("At least 1 test case failed. Check!")
finally:
    print("End of unit testing")