"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        current_lvl = []
        for i in range(rowIndex+1):
            row = [None for _ in range(i+1)]
            row[0],row[-1] = 1,1
            for j in range(1, len(row)-1):
                row[j] = current_lvl[i-1][j]+current_lvl[i-1][j-1]
            current_lvl.append(row)
        return current_lvl.pop()
print(Solution().getRow(2))
