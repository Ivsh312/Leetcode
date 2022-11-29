"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
"""
class Solution(object):
    @staticmethod
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = ['(','{','[']
        close_brackets = [')','}',']']
        for item, index in enumerate(s):
            if item in open_brackets:
                sub_str = s[index:]
                for sub_item in sub_str:
                    if sub_item in close_brackets and sub_item != close_brackets[close_brackets.index(sub_item)]:
                        return False


print(Solution().isValid('(){}[]'))
