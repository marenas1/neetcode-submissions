# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if (head.next == None):
            return False
        if (head.next.next == None):
            return False
        p1 = head
        p2 = head.next.next
        print(p2.val)
        while (p1 != p2):
            p1 = p1.next
            if (p2.next == None or p2.next.next == None):
                return False
            p2 = p2.next.next
        return True
        