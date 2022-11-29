"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        n+=1
        def get_combo(combo,start_val):
            if len(combo) == k:
                result.append(combo[:])
                return
            for i in range(start_val, n):
                combo.append(i)
                get_combo(start_val=i+1, combo=combo)
                combo.pop()
        get_combo(combo=[], start_val=1)
        return result
print(Solution().combine(4,2))