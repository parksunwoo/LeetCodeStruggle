from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        #start, end 지정
        for _ in range(m -1):
            start = start.next
        end = start.next
        
        for _ in range(n -m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
            
                          
if __name__ == '__main__':
    # begin
    s = Solution()
    head = [1,2,3,4,5]
    left = 2
    right = 4
    print (s.reverseBetween(head, left, right))
    # Output: [1,4,3,2,5]
