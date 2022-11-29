"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Type, Optional


class ListNode:
    def __init__(self, val: int=0, next = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, first: ListNode = None, last: ListNode = None):
        self.first = first
        self.last = last

    def add(self, val: int):
        if self.first is None:
            self.first = ListNode(val=val)
        elif self.last is None:
            self.last = ListNode(val=val)
            self.first.next = self.last
        else:
            self.last.next = ListNode(val=val)
            self.last = self.last.next

    def add_list_to_linked_list(self, node_values:[int]):
        for node in node_values:
            self.add(node)
        return self

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        current_data = self.current.val
        self.current = self.current.next
        return current_data


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_header = ListNode()
        next_node = result_header
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                next_node.next = l1
                l1=l1.next
            else:
                next_node.next = l2
                l2=l2.next
            next_node = next_node.next
        if l1:
            next_node.next=l1
        elif l2:
            next_node.next=l2
        # next_node.next = ListNode()
        return result_header.next

s = Solution()
a = LinkedList().add_list_to_linked_list([1,3,5]).first
b = LinkedList().add_list_to_linked_list([2,4,6]).first
linked_list = LinkedList()
linked_list.first = s.mergeTwoLists(l1=a,l2=b)

for data in linked_list:
    print(data)