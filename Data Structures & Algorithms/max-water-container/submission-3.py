class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        left_max = heights[left]
        right_max = heights[right]
        water = 0

        while left < right:
            width = right - left
            height = min(left_max, right_max)
            volume = width * height
            water = max(water, volume)

            if left_max > right_max:
                right -= 1
                right_max = heights[right]
            else:
                left += 1
                left_max = heights[left]

        return water
                