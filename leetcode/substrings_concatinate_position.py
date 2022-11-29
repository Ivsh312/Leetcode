"""
ou are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""
import collections
from itertools import permutations
from typing import List


class Solution:
    @staticmethod
    def findSubstring(s: str, words: List[str]) -> List[int]:
        if not words: return []
        len_str = len(s)
        len_word = len(words[0])
        count_words = len(words)
        len_combo = len_word*count_words
        count_repeat_words = {}
        for word in words:
            count_repeat_words[word]=count_repeat_words.get(word,0)+1
        results_start = []
        for _ in range(len_str-len_combo+1):
            sub_str = s[_:_+len_combo]
            sub_words_for_sub_str = [sub_str[i:i+len_word] for i in range(0,len_combo,len_word)]
            sub_count_repeat_words = {}
            for word in sub_words_for_sub_str:
                sub_count_repeat_words[word]=sub_count_repeat_words.get(word,0)+1
            if count_repeat_words == sub_count_repeat_words:
                results_start.append(_)
        return results_start

        # return word_dict
print(Solution.findSubstring("wordgoodgoodgoodbestword",
    ["word","good","best","good"]))