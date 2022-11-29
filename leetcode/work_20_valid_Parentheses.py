class Solution:

    def isValid(self, s: str) -> bool:
        open_brackets = {'{':'}','(':')','[':']'}
        list_oppening = []
        for item in s:
            if item in open_brackets:
                list_oppening.append(item)
            elif len(list_oppening) > 0 and open_brackets[list_oppening[-1]] == item:
                list_oppening.pop()
            else:
                return False
        return len(list_oppening) == 0
print(Solution().isValid('{'))
