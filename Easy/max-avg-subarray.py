from statistics import mean
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculating the sum of first k 
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        # Looping to keep a track of sum of contiguous array
        for i in range(k,len(nums)):
            # Adding the next and removing the first element of subarray
            cur_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, cur_sum)

        return max_sum/k