class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initializing the left pointer and counting zeroes
        left, zeroes_count = 0, 0 
    
        # Iterating the right index of the array
        for right in range(len(nums)):
            # Counting zeroes in arrays
            if nums[right] == 0:
                zeroes_count += 1

            # Making sure there are at most 1 zero
            if zeroes_count > 1:
                if nums[left] == 0:
                    zeroes_count -= 1
                left += 1

        return right-left

            
                

            
            