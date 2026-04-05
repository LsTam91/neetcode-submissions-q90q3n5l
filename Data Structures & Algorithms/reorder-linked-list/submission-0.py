# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        f, s = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
        
        def reverse(ll: Optional[ListNode]):
            prev, curr = None, ll
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        rev_head = s.next
        s.next = None
        s = reverse(rev_head)

        first, second = head, s
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
