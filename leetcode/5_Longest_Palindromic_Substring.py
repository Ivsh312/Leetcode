"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i in range(1, len(s)):
            index_neuborn = 1
            while i+index_neuborn < len(s) and i - index_neuborn >= 0:
                if s[i+index_neuborn] == s[i-index_neuborn]:
                    if len(max_palindrome) < len(s[i-index_neuborn:i+index_neuborn]):
                        max_palindrome = s[i-index_neuborn:i+index_neuborn+1]
                    index_neuborn+=1
                else:
                    break
        return max_palindrome


s = "aoaoaaoaoa"
print(Solution().longestPalindrome(s))