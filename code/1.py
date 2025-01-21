from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            if target - num in nums[i+1:]:
                return [i, i + 1 + nums[i+1:].index(target-num)]
        return []

nums = [3,2,4]
target = 6

s = Solution()
print(s.twoSum(nums, target))


