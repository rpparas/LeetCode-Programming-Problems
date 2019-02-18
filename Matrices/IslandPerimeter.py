# Problem Statement: https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> 'int':
        perimeter = 0

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    # check if it has adjacent to determine how many sides to count
                    modifiers = [(-1,0), (1,0), (0,-1), (0,1)]

                    for m in modifiers:            
                        perimeter += self.count_out_of_bounds(grid, r + m[0], c + m[1])
                        perimeter += self.count_adjacent_to_water(grid, r + m[0], c + m[1])


        return perimeter

    def count_out_of_bounds(self, grid, row, col):
        return 1 if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) else 0

    def is_within_bounds(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

    def count_adjacent_to_water(self, grid, row, col):
        if self.is_within_bounds(grid, row, col):
            return 0 if grid[row][col] == 1 else 1
        return 0

# Test Cases
s = Solution()
assert s.islandPerimeter([[]]) == 0
assert s.islandPerimeter([[0]]) == 0
assert s.islandPerimeter([[1]]) == 4
assert s.islandPerimeter([[1,0],[1,0],[1,1]]) == 10
assert s.islandPerimeter([[0,1,1]]) == 6
assert s.islandPerimeter([[0,0],[0,0]]) == 0
assert s.islandPerimeter([[0,1,1],[1,1,1]]) == 10
assert s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
print("Passed all test cases. Yay!")