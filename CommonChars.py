# Problem Statement: https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, A):
        if not A:
            return []

        common = {}
        for i in A[0]:
            common[i] = common[i] + 1 if i in common else 1

        for i in range(1, len(A)):
            temp_common = {}
            for i in A[i]:
                temp_common[i] = temp_common[i] + 1 if i in temp_common else 1
            for i in list(temp_common):
                if i in common:
                    temp_common[i] = min(common[i], temp_common[i])
                else:
                    temp_common.pop(i)
            common = temp_common

        result = []
        for i in common:
            count = common[i]
            while count > 0:
                result.append(i)
                count -= 1
        return result



sol = Solution()
result = sol.commonChars(["bella","label","roller"])
print(result)
result = sol.commonChars(["cool","lock","cook"])
print(result)