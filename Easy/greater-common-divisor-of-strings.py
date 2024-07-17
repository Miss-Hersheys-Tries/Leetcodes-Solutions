class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Determinig the lengths of both strings
        l1 = len(str1)
        l2 = len(str2)

        #Applying Euclidean's Algorithm
        def gcd(a, b):
            while b:  
                a, b = b, a % b  
            return a  

        # Checks for the NO GCD case
        if str1 + str2 != str2 + str1:
            return ""

        # Returns the GCD of the string
        return str1[:gcd(l1, l2)]

             