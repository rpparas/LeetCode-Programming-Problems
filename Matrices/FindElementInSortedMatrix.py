# Problem Statement: Given an M x N matrix in which each row and each column is sorted in ascending order , write a method to find an element.
# Also available on Leetcode: https://leetcode.com/problems/search-a-2d-matrix/

class FindElementInSortedMatrix():
    def find(self, matrix, element):
        if len(matrix) == 0:
            return False

        # process of elimination
        # let's start by eliminating rows/columns where we know the value isn't gonna be there

        # we can start on the top-right corner

        current_col = len(matrix[0]) - 1
        current_row = 0

        while current_col >= 0 and current_row < len(matrix):
            if element < matrix[current_row][current_col]:
                current_col -= 1 # move one column from the right
            elif element > matrix[current_row][current_col]:
                current_row += 1 # move one row from the top
            else: 
                return True # yay, we found it!


        return False



    def find2(self, matrix, element):
        if len(matrix) == 0:
            return False

        current_col = 0
        current_row = len(matrix) - 1

        while current_col < len(matrix[0]) and current_row >= 0:
            if element > matrix[current_row][current_col]:
                current_col += 1 # move one column from the left
            elif element < matrix[current_row][current_col]:
                current_row -= 1 # move one row from the bottom
            else: 
                return True # yay, we found it!


        return False


s = FindElementInSortedMatrix()
input = [[1,2,6,8], [2,5,8,12], [3,7,11,14] ,[4,9,15,16]]
print(s.find(input, 11))
print(s.find2(input, 11))


