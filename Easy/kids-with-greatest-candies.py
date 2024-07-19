class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Finding the max number of candies from initial list
        maxCandies = max(candies)
        # Creating a new list to store boolean values
        moreCandies = []
        # Looping to find whether greater or less
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                moreCandies.append(True)
            else:
                moreCandies.append(False)
        return moreCandies
    
