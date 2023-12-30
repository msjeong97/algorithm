# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         solution = [10000] * len(nums)
#         solution[0] = 0

#         for i in range(len(nums)):
#             num = nums[i]
#             for j in range(num + 1):
#                 if i + j >= len(nums):
#                     break
                
#                 solution[i + j] = min(solution[i + j], solution[i] + 1)
        
#         return solution[len(nums) - 1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        curMax = 0
        nextMax = 0

        for i in range(len(nums) -1):
            nextMax = max(nums[i] + i, nextMax)

            if nextMax >= len(nums) - 1:
                count = count + 1
                break

            if i == curMax:
                count = count + 1
                curMax = nextMax

        return count
