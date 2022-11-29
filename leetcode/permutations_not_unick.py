"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
# import time
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        self.findPermutations(nums,[])
        return self.result


    def findPermutations(self, nums, combination):
        if nums==[]:
            self.result.append(combination)
            return
        for i in range(len(nums)):
            nums_i = nums[i]
            if i > 0 and nums_i == nums[i-1]:
                continue
            combination.append(nums_i)
            self.findPermutations(nums[:i]+ nums[i+1:], combination[:])
            combination.pop()
for i in Solution().permuteUnique([1,2,1]):
    print(i)
