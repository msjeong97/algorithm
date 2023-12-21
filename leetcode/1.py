class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()

        for i, num in enumerate(nums):
            cand = target - num

            if cand in table.keys():
                return [i, table[cand]]
            else:
                table[num] = i

