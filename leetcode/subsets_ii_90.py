"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List

def get_subsets(next_start,current_set, result, nums):
    result.append(current_set[:])
    for i in range(next_start,len(nums)):
        if i > next_start and nums[i]==nums[i-1]:
            continue
        get_subsets(i+1, [nums[i]]+current_set, result, nums)
    return result
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return get_subsets(0, [], [], nums)


print(Solution().subsetsWithDup([1,2,2]))