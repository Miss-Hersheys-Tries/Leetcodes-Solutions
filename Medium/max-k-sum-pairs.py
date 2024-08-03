class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sorting the array 
        nums.sort()
        operations = 0
        i, j = 0, (len(nums)-1)

        # Iterating the array until every element is checked
        while i < j :
            cur_sum = nums[i] + nums[j]
            # Iterate both index if sum is found
            if cur_sum == k:
                operations += 1
                i += 1
                j -= 1
            # Iterate towards increasing value if sum is less
            elif cur_sum < k:
                i += 1
            # Iterate towards decreasing value if sum is greater
            else:
                j -= 1
    
        return operations
