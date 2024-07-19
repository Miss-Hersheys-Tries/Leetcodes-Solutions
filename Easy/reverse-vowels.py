class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l = len(s)
        # Converting the string to a list to ease the vowels swaps
        sList = list(s)
        #Creating two pointers left and right to track chars from front and end
        left , right = 0, l-1
        # Looping until both pointers meet in somewhere middle
        while left < right:
            # Swapping if both pointers are vowels
            if (sList[left] in vowels) and (sList[right] in vowels):
                sList[left], sList[right] = sList[right], sList[left]
                left += 1
                right -= 1
            # Moving the right pointer if left is a vowel
            elif sList[left] in vowels:
                right -= 1
            # Moving the left pointer if right is a vowel
            elif sList[right] in vowels:
                left += 1
            # Moving both pointers if none are vowels
            else:
                left += 1
                right -= 1

        return "".join(sList)


            

        
