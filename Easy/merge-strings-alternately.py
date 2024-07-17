class Solution:
    def mergeAlternately( self, word1: str, word2: str) -> str:
        # Determinig the length of each words
        l1 = len(word1)
        l2 = len(word2)

        # Adding the extra length of longer word l1
        if l1 > l2:
            return self.mergeEquals( word1[:l2], word2) + word1[l2:]
        # Adding the extra length of longer word l2 
        elif l1 < l2:
            return self.mergeEquals( word1, word2[:l1]) + word2[l1:]
        # Simply merging words of equal lengths
        else:
            return self.mergeEquals( word1, word2)

    # Slicing and joining equal length strings
    def mergeEquals(self, word1, word2):
        l = len(word1)
        string =""
        for i in range(l):
            string += word1[i:i+1] + word2[i:i+1]

        return string


