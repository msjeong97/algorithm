class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left = 0 
        right = len(height) - 1

        while(left < right):
            x = right - left
            y = min(height[left], height[right])
            maxWater = max(maxWater, x * y)

            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        
        return maxWater
