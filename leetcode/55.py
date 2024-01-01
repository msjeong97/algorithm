class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxDistance = 0

        for i in range(len(nums)):
            maxDistance = max(nums[i] + i, maxDistance)

            if maxDistance >= len(nums) - 1:
                return True
            if i >= maxDistance:
                return False
        
        return False
