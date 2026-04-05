# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        else:
            run = head.next
        walk = head
        while run:
            if run.val == walk.val:
                return True
            else:
                run = run.next
                walk = walk.next
                if not run:
                    return False
                else:
                    run = run.next
        return False
            