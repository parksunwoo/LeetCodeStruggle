from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # cur = head
        # while cur and cur.next:
            # cur.val, cur.next.val = cur.next.val, cur.val
            # cur = cur.next.next
        # return head
        
        # root = prev = ListNode(None)
        # prev.next = head
        # while head and head.next:
            # b = head.next
            # head.next = b.next
            # b.next = head
            
            # prev.next = b
            
            # head = head.next
            # prev = prev.next.next
        # return root.next
        
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
        
        
if __name__ == '__main__':
    # begin
    s = Solution()
    head = [1,2,3,4]
    print(s.swapPairs(head))
    # Output: [[2,1,4,3]
