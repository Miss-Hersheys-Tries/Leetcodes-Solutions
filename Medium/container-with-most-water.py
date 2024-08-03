class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Assigning two pointers
        left, right = 0, len(height)-1

        max_area = 0

        # Looping until pointers meet in middle
        while left < right:
            # Product of min of height & length
            area = min(height[left], height[right]) * (right-left)
            max_area = max(area, max_area)

            # Shifting the pointer of shorter height towards the longer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area 