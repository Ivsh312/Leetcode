import functools
from itertools import count, islice
from math import sqrt, modf


class Solution(object):

    @staticmethod
    def isThree(n):
        """
        :type n: int
        :rtype: bool
        """
        sqr = sqrt(n)
        if modf(sqr)[0]!=0.0 or n < 2:
            return False
        prime = (lambda n:n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1))))(sqr)
        if prime:
            return True
        return False


print(Solution().isThree(4))
