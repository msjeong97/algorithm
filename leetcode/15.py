class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = list()
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSumValue = nums[i] + nums[left] + nums[right]

                if threeSumValue == 0:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    
                    left = left + 1
                    right = right - 1
                elif threeSumValue > 0:
                    right = right - 1
                else:
                    left = left + 1
            
        return results
