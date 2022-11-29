from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int):
        stay = 0
        if nums == []:
            return 0
        for index,item in enumerate(nums):
            if item != val:
                nums[stay] = nums[index]
                stay +=1
        return stay
nums = [2]
print(Solution().removeElement(nums,
3))
print(nums)