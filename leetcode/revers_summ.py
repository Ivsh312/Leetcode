"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Node:
    def __init__(self,data = None, next = None):
        self.data=data
        self.next=next
def get_next(list_li: ListNode):
    current_value = list_li
    while True:
        yield current_value.val
        current_value = current_value.next
        if current_value is None:
            break

class ListLinked:

    def __init__(self):
        self.first = None
        self.last = None

    def add_node(self, data):
        if self.first is None:
            self.first = Node(data)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(data)
            self.first.next = self.last
        else:
            current = Node(data)
            self.last.next = current
            self.last = current

    def __iter__(self):
        self.current_item = self.first
        return self

    def __next__(self):
        if self.current_item is None:
            raise StopIteration
        current_data = self.current_item.data
        self.current_item = self.current_item.next
        return current_data


class Solution(object):
    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        count = 0
        a = get_next(l1)
        b = get_next(l2)
        l11 = []
        l22 = []
        for i in a:
            l11.append(i)
        for i in b:
            l22.append(i)
        long_l, short_l = (l11, l22) if len(l11) > len(l22) else (l22,l11)
        summ = [None] * len(long_l)
        for index, value in enumerate(long_l):
            if index < len(short_l):
                summ[index] = value+count+short_l[index]
            else:
                summ[index]=value+count
            count = 0
            if summ[index]>10:
                summ[index] -= 10
                count = 1
        if count == 1:
            summ.append(1)
bufer = [1,2,3,4,5]
list_nods = []
for i in bufer:
    list_nods.append(ListNode(i))
for index in range(len(list_nods)-1):
    list_nods[index].next=list_nods[index+1]

list_nod_1 = ListNode(1)
list_nod_2 = ListNode(93)
list_nod_3 = ListNode(8889)
list_nod_1.next=list_nod_2
list_nod_2.next=list_nod_3


# Solution.addTwoNumbers([9,2,4],[4,3,9])
# list1 = ListLinked()
# list1.add_node(1)
# list1.add_node(2)
# list1.add_node(3)
# list1.add_node(4)
# print(next(list1))
# print(next(list1))
# print(next(list1))
# print(next(list1))
# for _ in list1:
#     print(_)


# class Fibbonachi:
#     def __init__(self):
#         print('a')
#
#     def __iter__(self):
#         print('b')
#         self.cur_val = 0
#         self.next_val = 1
#         return self
#
#     def __next__(self):
#         tmp = self.next_val
#         self.next_val += self.cur_val
#         self.cur_val = tmp
#         return tmp
# a = Fibbonachi()
# print(next(a))



"""

my solution:

def get_next(list_li):
    current_value = list_li
    while True:
        yield current_value.val
        current_value = current_value.next
        if current_value is None:
            break
class Solution(object):
    @staticmethod
    def addTwoNumbers(l1, l2):
  
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode

count = 0
l11 = [i for i in get_next(l1)]
l22 = [i for i in get_next(l2)]
long_l, short_l = (l11, l22) if len(l11) > len(l22) else (l22,l11)
summ = [None] * len(long_l)
for index, value in enumerate(long_l):
    if index < len(short_l):
        summ[index] = value+count+short_l[index]
    else:
        summ[index]=value+count
    count = 0
    if summ[index]>=10:
        summ[index] -= 10
        count = 1
if count == 1:
    summ.append(1)
list_nods = []
list_nods = [ListNode(i) for i in summ]
for index in range(len(list_nods)-1):
    list_nods[index].next=list_nods[index+1]
return list_nods[0]
"""




