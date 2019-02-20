# Problem Statement: https://leetcode.com/problems/group-anagrams/

import collections

class Solution():

    # Assume input is all alphabetical letters and some spaces, no numbers
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':

        # using bucket sort to keep track of "anagram signatures" and noting their index in hashmap with 
        # "anagram's concatenation of letters" as key and list/array of indices as values

        unique_anagram = {}
        max_frequency = 0
        output = []

        for i, word in enumerate(strs):
            sig = self.get_anagram_signature(word)
            if sig in unique_anagram:
                unique_anagram[sig] += [i]
            else:
                unique_anagram[sig] = [i]

            if len(unique_anagram[sig]) > max_frequency:
                max_frequency = len(unique_anagram[sig])


        for sig, array in unique_anagram.items():
            o = []
            for i in array:
                o.append(strs[i])
            output.append(o)

        return output

            

    def get_anagram_signature(self, word):
        # ignore/remove all spaces and extra chars
        # sort letters in word using OrderedDictionary

        d = collections.OrderedDict()
        for w in word:
            w = w.lower()
            if w in d:
                d[w] = d[w] + 1
            else:
                d[w] = 1

        # assume sorting letters is done via QuickSort, otherwise, write our own function?
        d = collections.OrderedDict(sorted(d.items()))
        output = ""
        for i, k in d.items():
            output += i * k
        return output


# Test Cases

s = Solution()
print(s.groupAnagrams([]))
print(s.groupAnagrams(["", ""]))
print(s.groupAnagrams([" "]))
print(s.groupAnagrams(["a", "b"]))
print(s.groupAnagrams(["b", "b"]))
print(s.groupAnagrams(["zebra", "I", "Moon starer", "Dormitory", "DirtY Room", "astronomer", "not"]))
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
