# Problem Statement: https://leetcode.com/problems/number-of-islands/

class Solution:
    def count_islands(self, grid: 'List[List[str]]') -> 'int':
        if len(grid) == 0:
            return 0

        num_contiguous_islands = 0
        modifiers = [(-1,0), (1,0), (0,-1), (0,1)]

        for r, row in enumerate(grid):
            for c, val in enumerate(row):

                #find our first island
                if self.is_island(grid, r, c):
                    grid[r][c] = 0

                    # identify if adjacent cells are part of this island
                    # depth-first search to find adjacent cells/islands

                    breadth = 1
                    stack = []

                    r2 = r  # using another variable so we dont override the matrix iteration
                    c2 = c

                    while len(stack) > 0 or breadth == 1:
                        if len(stack) > 0:
                            tup = stack.pop()
                            r2 = tup[0]
                            c2 = tup[1]

                        for m in modifiers:
                            if self.is_within_bounds(grid, r2 + m[0], c2 + m[1]):
                                if self.is_island(grid, r2 + m[0], c2 + m[1]):
                                    grid[r2 + m[0]][c2 + m[1]] = 0
                                    stack.append((r2 + m[0], c2 + m[1]))

                        breadth += 1

                    num_contiguous_islands += 1

        return num_contiguous_islands


    def is_within_bounds(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

    def is_island(self, grid, row, col):
        return grid[row][col] == 1

try:
    s = Solution();
    assert s.count_islands([[]]) == 0
    assert s.count_islands([[]]) == 0
    assert s.count_islands([[0]]) == 0
    assert s.count_islands([[1]]) == 1
    assert s.count_islands([[1,0], [1,0], [1,1]]) == 1
    assert s.count_islands([[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]) == 6
    assert s.count_islands([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 1
    print("Passed all test cases. Yay!")
except AssertionError:
    print("One of the test cases failed. Check!")
finally:
    print("End of test")