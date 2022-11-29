"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.





Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List

phone_dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

class Solution:
    """  """
    def letter_combinations(self, digits: str) -> List[str]:
        ""
        if digits=="":
            return []
        len_digits = len(digits)
        result = []
        def get_combo(str_comb, start_val):
            if len(str_comb) == len_digits:
                cobo_str = ''.join(str_comb)
                result.append(cobo_str)
                return
            for i in phone_dict[digits[start_val]]:
                str_comb +=i
                get_combo(str_comb, start_val+1)
                str_comb = str_comb[:-1:]
        get_combo("",0)
        return result
print(Solution().letterCombinations("23"))