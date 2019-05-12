# Problem Statement: https://leetcode.com/problems/top-k-frequent-words/

from collections import defaultdict

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        counter = defaultdict(int)

        for w in words:
            counter[w] += 1

        byCount = defaultdict(list) #will always be 4
        topCount = 0

        for word, freq in counter.items():
            if len(byCount[freq]) < k: # add if length at count is
                byCount[freq].append(word)
                byCount[freq].sort()
            elif word < byCount[freq][-1]: # we remove the last word in the alphabetical order
                byCount[freq].pop(-1)
                byCount[freq].append(word)
                byCount[freq].sort()
            if freq > topCount:
                topCount = freq


        result = []
        while topCount > 0 and len(result) < k:
            toConsider = byCount[topCount]
            for x in toConsider:
                result.append(x)
                if len(result) >= k:
                    break
            topCount -= 1

        return result



s = Solution()
assert s.topKFrequent(["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"], 1) == ["fvvdtpnzx"]