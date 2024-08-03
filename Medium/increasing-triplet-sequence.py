class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initializing the first two numbers with greatest of them
        first, second = max(nums) + 1, max(nums) + 1

        for num in nums:
            # First number is the smallest
            if num <= first:
                first = num
            # Second number is greater than first
            elif num <= second:
                second = num
            # True if number is not smaller than first two (ie. greatest)
            else: 
                return True

        return False
