"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""

from typing import List
class Solution:
    def get_combo(self, combo, values):
        for index in range(len(values)):
            val = values[index]
            if val in combo:
                continue
            combo.append(val)
            if len(combo) == self.len_l:
                self.result.append(combo[:])
                combo.pop()
                return
            self.get_combo(combo,values[:index]+values[index+1:])
            combo.pop()
    def permute(self, l: List[int]) -> List[List[int]]:
        self.result = []
        self.len_l = len(l)
        self.get_combo([],l)
        return self.result
for i in Solution().permute([1,2,3]):
    print(i)