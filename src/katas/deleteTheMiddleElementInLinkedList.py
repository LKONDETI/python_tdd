from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#time is O(n) and space is O(1)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = prev.next.next
        return head
        