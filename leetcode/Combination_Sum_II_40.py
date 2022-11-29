"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        len_candidates = len(candidates)
        if sum(candidates)<target:
            return []
        candidates.sort()

        def get_combo(combo,start_val, new_target):
            if new_target == 0:
                result.append(combo[:])
                return
            if new_target < 0:
                return
            for i in range(start_val, len_candidates):
                if i > start_val and candidates[i-1] == candidates[i]:
                    continue
                elif new_target - candidates[i] >= 0:
                    combo.append(candidates[i])
                    get_combo(start_val=i+1, combo=combo, new_target = new_target - candidates[i])
                    combo.pop()
                else:
                    return
        get_combo(combo=[], start_val=0, new_target = target)
        return result
print(Solution().combinationSum2([4,4,2,1,4,2,2,1,3],
6))