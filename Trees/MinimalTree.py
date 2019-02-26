class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def create_minimal_tree(self, sorted_list):
        if not sorted_list:
            return None
        # since list is sorted, we can start at the middle and build out the tree from the center of the list
        # then keep dividing remaining numbers in list

        mid = len(sorted_list) // 2
        tree = TreeNode(sorted_list[mid])
        tree.left = self.insert_node(sorted_list, 0, mid - 1)
        tree.right = self.insert_node(sorted_list, mid + 1, len(sorted_list) - 1)

        return tree

    def insert_node(self, sorted_list, start, end):
        if start > end:
            return None

        mid = (end + start) // 2
        tree = TreeNode(sorted_list[mid])
        tree.left = self.insert_node(sorted_list, start, mid-1)
        tree.right = self.insert_node(sorted_list, mid+1, end)
        return tree


    def print_bfs(self, tree):
        queue = [tree]

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)


    def print_pre_order(self, tree):
        if tree:
            print(tree.val)
            self.print_pre_order(tree.left)
            self.print_pre_order(tree.right)

    def print_in_order(self, tree):
        if tree:
            self.print_pre_order(tree.left)
            print(tree.val)
            self.print_pre_order(tree.right)


sol = Solution()
# tree = sol.create_minimal_tree([1,2,3,4,5,6])
# tree = sol.create_minimal_tree(range(0,12))
# tree = sol.create_minimal_tree(None)
# sol.print_bfs(tree)

# tree = sol.create_minimal_tree([1,3])
# tree = sol.create_minimal_tree([-1,0,1,2])

tree = sol.create_minimal_tree([-93,-89,-85,-76,-56,-53,-20,-10,20,28,41,50,66,70,87,88,91,94])
sol.print_bfs(tree)
