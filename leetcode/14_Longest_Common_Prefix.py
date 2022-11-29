from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len_repit = min([len(item) for item in strs])
        equal_prefix = []
        for index in range(max_len_repit):
            pattern = strs[0][index]
            if not all([item[index] == pattern for item in strs]):
                break
            equal_prefix.append(pattern)
        return ''.join(equal_prefix)
print(Solution().longestCommonPrefix(
    [
        'asd','as','as'
    ]
))