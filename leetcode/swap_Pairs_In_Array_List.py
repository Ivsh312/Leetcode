# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if(head == None or head.next == None ):
#             return head
#         prev = head
#         curr = head.next
#         curr1 = curr
#         head = curr
#         while True :
#             next_node = curr.next
#             curr.next = prev
#             if(next_node == None or next_node.next == None):
#                 prev.next = next_node
#                 break
#             prev.next = next_node.next
#             prev = next_node
#             curr = next_node.next


class Solution(object):
    @staticmethod
    def swapPairs(head):
        current_node = head
        link_from_current = head.next
        new_head = link_from_current
        while True:
            link_from_next = link_from_current.next
            link_from_current.next = current_node
            if link_from_next is None or link_from_next.next is None:
                current_node.next = link_from_next
                break
            current_node.next = link_from_next.next
            current_node = link_from_next
            link_from_current = link_from_next.next


        return new_head
        #     current = head
        #     next_v = head.next
        #     new_haed = next_v
        # while True:
        #     next_next_v = next_v.next
        #     next_v.next = current
        #     if next_next_v == None or next_next_v.next == None:
        #         current.next = next_next_v
        #         break
        #     current.next = next_next_v.next
        #     current = next_next_v
        #     next_v = next_next_v.next
        #
        #
        #
        #
        # return curr1