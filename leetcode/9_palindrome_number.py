class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return 0
        right = []
        b = x%10
        while x>0:
            right.append(b)
            x //=10
            b = x%10
            # b = x-(b*pow(10,i))
        len_b = len(right)
        for i in range(len_b//2):
            try:
                if right[i]!=right[len_b-i-1]:
                    return 0
            except IndexError:
                print(i, len_b-1,right)
        return 1
print(Solution().isPalindrome(1001))