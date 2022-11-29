"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from typing import List



class Solution:
    sudocky_size = 3
    def isValidSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        result_size = len(board)//self.sudocky_size*self.sudocky_size
        row = [set() for i in range(result_size)]
        column = [set() for i in range(result_size)]
        subset = [set() for i in range(result_size)]
        for i in range(result_size):
            for j in range(result_size):
                board_elem = board[i][j]
                if board_elem =='.':
                    continue
                else:
                    if board_elem in row[i]:
                        return False
                    if board_elem in column[j]:
                        return False
                    subset_index = (i//self.sudocky_size)*self.sudocky_size + j//self.sudocky_size
                    if board_elem in subset[subset_index]:
                        return False
                    column[j].add(board_elem)
                    row[i].add(board_elem)

                    subset[subset_index].add(board_elem)
        return True

print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],
                              ["6",".",".","1","9","5",".",".","."],
                              [".","9","8",".",".",".",".","6","."],
                              ["8",".",".",".","6",".",".",".","3"],
                              ["4",".",".","8",".","3",".",".","1"],
                              ["7",".",".",".","2",".",".",".","6"],
                              [".","6",".",".",".",".","2","8","."],
                              [".",".",".","4","1","9",".",".","5"],
                              [".",".",".",".","8",".",".","7","9"]]))