class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        # Initializing all the required lists
        left_product = [1]*l
        right_product = [1]*l
        answer = [1]*l
        # Calculating the product of left side of each number
        for i in range(1, l):
            left_product[i] = left_product[i-1] * nums[i-1]
        # Calculating the product of right side of each number
        for i in range(l-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
        # Calculating total product
        for i in range(l):
            answer[i] = left_product[i] * right_product[i] 
        return answer

