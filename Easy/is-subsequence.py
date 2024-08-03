class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Assign index for each string
        i, j = 0, 0 

        # Iterate until every element of t is checked
        while i < len(s) and j < len(t):
            # Iterate if elements are same in both
            if s[i] == t[j]:
                i += 1
            j += 1

        # Return true if all elements of s are found in t
        return i == len(s)