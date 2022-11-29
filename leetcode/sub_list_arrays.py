"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
Example 3:

Input: nums = []
Output: []
Example 4:

Input: nums = [-1]
Output: ["-1"]
Example 5:

Input: nums = [0]
Output: ["0"]
"""
from cmath import inf


def check_delta_is_one(a,b):
    return b-a== 1
def to_str(var1,var2=None):
    print(var1,var2)
    if var2 and var1!=var2:
        return f'{var1}->{var2}'
    return f'{var1}'

class Solution(object):
    @staticmethod
    def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        list_sub_array =[]
        nums.appent(inf)
        start = nums[0]
        last = start
        for item in nums:
            if check_delta_is_one(last, item):
                last = item
            else:
                if start != item:
                    list_sub_array.append(to_str(start, last))
                start = item
                last = item
        return list_sub_array
print(Solution().summaryRanges([-2,-1]))

# while i < max_index_nums:
#     cur = nums[i]
#     differ_by_one = 1
#     while i+differ_by_one <= max_index_nums and compare_two(nums[i+differ_by_one-1],nums[i+differ_by_one]):
#         differ_by_one+=1
#     list_sub_array.append(to_str(cur, nums[i+differ_by_one-1]))
#     i+=differ_by_one
#     if i == max_index_nums:
#         list_sub_array.append(to_str(nums[i]))
#         return list_sub_array