class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Initializing the left pointer 
        left = 0
    
        # Iterating the right index of the array
        for right in range(len(nums)):
            # Reducig the number of possible zeroes to flip as iterate
            if nums[right] == 0:
                k -= 1

            # Increasing left index and increasing possible zeroes to flip
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right-left+1

        

        
        


