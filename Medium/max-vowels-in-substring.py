class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Using a set for O(1) look-up time
        vowels = set('aeiou') 
        max_vowels = 0
        count = 0
        
        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        # Initialize max_vowels with the count from the first window
        max_vowels = count
        
        # Slide the window from the end of the first window to the end of the string
        for i in range(k, len(s)):
            # If the character at the start of the previous window is a vowel, decrement the count
            if s[i - k] in vowels:
                count -= 1
            # If the character at the end of the current window is a vowel, increment the count
            if s[i] in vowels:
                count += 1
            # Update the maximum number of vowels found
            max_vowels = max(max_vowels, count)
        
        return max_vowels

