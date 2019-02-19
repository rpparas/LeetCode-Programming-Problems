# Problem Statement: https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: 'List[int]') -> 'List[int]':
        odd = -1
        even = -1

        for i in range(len(A)):
            if i % 2 == 1:
                if A[i] % 2 != 1:
                    odd = self.find_odd(A, odd+1)
                    A[i], A[odd] = A[odd], A[i]
            else:
                if A[i] % 2 == 1:
                    even = self.find_even(A, even+1)
                    A[i], A[even] = A[even], A[i]

        # print(A)
        return A

    def find_odd(self, A, odd):
        while odd < len(A):
            if A[odd] % 2 == 1 and odd % 2 == 0:
                return odd
            odd += 1
        return odd


    def find_even(self, A, even):
        while even < len(A):
            if A[even] % 2 == 0 and even % 2 == 1:
                return even
            even += 1    
        return even

s = Solution()
s.sortArrayByParityII([1,2])
s.sortArrayByParityII([1,0,4,3])
s.sortArrayByParityII([1,0])
s.sortArrayByParityII([4,2,5,7])
