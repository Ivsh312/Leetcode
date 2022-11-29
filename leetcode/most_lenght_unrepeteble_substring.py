class Solution(object):
    @staticmethod
    def lengthOfLongestSubstring(s:str)->int:
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        max_str_len = 0
        sub_str = ""
        for symbol_1 in s:
            if symbol_1 in sub_str:
                sub_str = sub_str[sub_str.index(symbol_1)+1:]
            sub_str+=symbol_1
            max_str_len = max(max_str_len,len(sub_str))
        return max_str_len
print(Solution.lengthOfLongestSubstring("aabaab!bb"))











        #     if current is None or current == symbol_1:
        #         current = symbol_1
        #         continue
        #     else:
        #         max_len +=1
        #
        #
        #
        #
        #
        # sub_strigs = [None]*len(s)
        # for index_1, simble_1 in enumerate(s):
        #     sub_string = []
        #     next_simles = s[index_1:]
        #     for index_2, simble_2 in enumerate(next_simles):
        #         if simble_2 in sub_string and index_2!=index_1:
        #             break
        #         sub_string.append(simble_2)
        #     sub_strigs[index_1] = len(sub_string)
        # max_len=max(sub_strigs)
        # return max_len

# class Solution(object):
#     @staticmethod
#     def lengthOfLongestSubstring(s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         status = dict()
#         maxlength = 0
#         start = 0
#         for index, char in enumerate(s):
#             print('iter ', index, '------------------------------------------------------------')
#             print('status ',status)
#             if char in status and start <= status[char]:
#                 start = status[char]+1
#                 print('start ',start)
#             else:
#                 maxlength = max(maxlength, index-start+1)
#                 print('maxlength ',maxlength)
#             status[char] = index
#             print('status ',status)
#
#         return maxlength
# print(Solution.lengthOfLongestSubstring('addghghghghghghghghgh'))