class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)

        # Index of non zero elements 
        n = 0

        # First shifting all non zeroes to left of the list
        for i in range(l):
            if nums[i] != 0:
                nums[n] = nums[i]
                n += 1
        
        # Assigning 0 to rest of the list after non-zero elements are placed
        for i in range(n, l):
            nums[i] = 0