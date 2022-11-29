class Solution(object):
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        base = abs(x)
        revers_int = 0
        while base > 0:
            revers_int = revers_int*10 + base%10
            base //=10
        if revers_int>2**31 - 1:
            return 0
        if x<0:
            return revers_int*(-1)
        return revers_int


print(Solution().reverse(123))
