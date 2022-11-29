"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List


class Solution(object):
    @staticmethod
    def twoSum(nums:List, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_i,i in enumerate(nums):
            for index_j,j in enumerate(nums):
                if i+j-target==0 and index_i != index_j:
                    return index_i,index_j
print(Solution.twoSum([3,3], 6))

# a = [1,2,3,5]
# b = [1,1,1,1]
# for v,c,n in zip(a,b,range(len(a))):
#     print(v,c,n)
