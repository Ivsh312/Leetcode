"""
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.
"""
from typing import List


class Solution:
    """ for what it is."""

    @staticmethod
    def find_the_winner(n_friends: int, k_distance: int) -> int:
        """ for what it is. """
        circle = [i for i in range(n_friends)]
        k_distance -= 1
        current_index = 0
        while n_friends > 1:
            current_index = (current_index + k_distance) % n_friends
            circle.pop(current_index)
            n_friends -= 1
        return circle.pop() + 1


print(Solution().find_the_winner(n_friends=5, k_distance=3))


def summ(L1: List, L2: list):
    if len(L1) < len(L2):
        for i in range(len(L1)):
            L2[i] += L1[i]
