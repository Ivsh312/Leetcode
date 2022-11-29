# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self, list_vlues = None):
        self.first = None
        self.last = None
        if list_vlues is not None:
            for _ in list_vlues:
                self.add_node(_)
    def add_node(self, value)->None:
        if self.first is None:
            self.first = ListNode(value)
        elif self.last is None:
            self.last = ListNode(value)
            self.first.next = self.last
        else:
            self.last.next = ListNode(value)
            self.last = self.last.next
    def __iter__(self):
        self.current = self.first
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        carrent_val = self.current.val
        self.current = self.current.next
        return carrent_val



class Solution(object):
    @staticmethod
    def swapPairs(head):
        if head is None:
            return head
        if head.next is None:
            return head
        base = head.next.next
        current = head
        head = head.next
        head.next=current
        head.next.next = Solution().swapPairs(base)
        return head


    @staticmethod
    def swapPairs2(head):
        if head is None or head.next is None:
            return head
        next_start = head.next.next
        current_start = head
        next_n = head.next
        next_n.next = current_start
        current_start.next = Solution().swapPairs2(next_start)
        return next_n

    @staticmethod
    def swapPairs3(head):
        zero = ListNode(val=0,next=head)
        before, one, two = zero, zero.next, zero.next.next
        while two:
            buf_link_to_three = two.next
            two.next = one
            one.next = buf_link_to_three
            before.next = two

            before = one
            one = buf_link_to_three
            if one: two = one.next
            else: two = None

        return zero.next

a = LinkedList([-3,-2,-1,12,8,5])
for i in a:
    print(i)

# a = Solution.swapPairs3(a.first)
# next_v = a
# while True:
#     print(next_v.val)
#     next_v = next_v.next
#     if next_v is None:
#         break

# def f(param:int):
#
#     return param



