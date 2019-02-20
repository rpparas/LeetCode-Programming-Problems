import collections

class SortAnagrams():

    # Assume input is all alphabetical letters and some spaces, no numbers
    def sort(self, words):

        # using bucket sort to keep track of "anagram signatures" and noting their index in hashmap with 
        # "anagram's concatenation of letters" as key and list/array of indices as values

        unique_anagram = {}

        if len(words) <= 2:
            return A

        for i, word in enumerate(words):
            sig = self.get_anagram_signature(word)
            if sig in unique_anagram:
                unique_anagram[sig] += [i]
            else:
                unique_anagram[sig] = [i]

        output = []

        for sig, array in unique_anagram.items():
            for i in array:
                output.append(words[i])

        return output

            

    def get_anagram_signature(self, word):
        # ignore/remove all spaces and extra chars
        # sort letters in word using OrderedDictionary

        d = collections.OrderedDict()
        for w in word:
            if w.isalpha():
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

    




s = SortAnagrams()
word_cloud = ["zebra", "I", "Moon starer", "Dormitory", "DirtY Room", "astronomer", "not"]
result = s.sort(word_cloud)
print(result)